<link rel="stylesheet" href="src/routes/myprojects/styles.css">
<style>
  .delete-button {
  background-color: red;
  color: white;
  border: none;
  cursor: pointer;
}


</style>
<script lang='ts'>
	import { onMount } from 'svelte';

  let projects = [
    {
      id: generateRandomId(),
      name: 'Project 1 - Hand Gestures',
      description: 'Project that aims to detect hand gestures and classify them into different categories: thumbs up, thumbs down and peace. It can also extract features using MediaPipe.',
      image: 'src/routes/images/gradient.jpeg',
      link: '/project/acquisition',
      classes: ['Thumbsup', 'Thumbsdown'],
      role: 'Hand Sign 2',
      created: '3 months ago'
    },
    {
      id: generateRandomId(),
      name: 'Project 2 - Face Detection',
      description: 'This project can support face detection using the MediaPipe library. The feature extraction aims to detect the facial queues of the user detecting different face points.',
      image: 'src/routes/images/gradient2.jpeg',
      link: '/project/acquisition',
      classes: ['Peace', 'Thumbs', 'Pointing'],
      role: 'Hand-Sign 1',
      created: '6 months ago'
    },
    {
      id: generateRandomId(),
      name: 'Project 3 - Hand & Face Recognition',
      description: 'This project can support face  and also hand detection using the MediaPipe library. It is a combination of project 1 and 2 previously created',
      image: 'src/routes/images/gradient3.jpeg',
      link: '/project/acquisition',
      technologies: ['Smile', 'Sad', 'Goofy'],
      role: 'Facial Queues',
      created: '2 months ago'
    }
  ];

  let hasNewProjects = false;


  onMount(() => {
    const storedProjects = localStorage.getItem('projects');
    if (storedProjects) {
      projects = JSON.parse(storedProjects);
      checkNewProjects();
    }
  });

  // Function to generate a random ID
  function generateRandomId() {
    const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let id = '';
    for (let i = 0; i < 10; i++) {
      id += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return id;
  }

  function clearNewProjects() {
    if (confirm('Are you sure you want to clear the new projects?')) {  
      const storedProjects = localStorage.getItem('projects');
      if (storedProjects) {
        const parsedProjects = JSON.parse(storedProjects);
        const existingProjects = parsedProjects.slice(0, 3); // Get the first three projects
        const newProjects = parsedProjects.slice(3);

        localStorage.setItem('projects', JSON.stringify(existingProjects));
        projects = existingProjects
        hasNewProjects = false;

        const projectList = document.querySelector("#project_list");
        projectList.innerHTML = "";

        projects.forEach((project) => {
          appendProjectCard(project);
        });

        adjustProjectCardsLayout(); 
        checkNewProjects(); 
      }
    }
  }


  function checkNewProjects() {
    const storedProjects = localStorage.getItem('projects');
    if (storedProjects) {
      let parsedProjects = JSON.parse(storedProjects);
      if (parsedProjects.length > 3) {
        hasNewProjects = true;
      } else {
        hasNewProjects = false;
      }
    }
    adjustProjectCardsLayout();
  }





  function createGradientPictureURL(colors) {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    canvas.width = 200; // Set the desired width
    canvas.height = 200; // Set the desired height

    const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < colors.length; i++) {
      gradient.addColorStop(i / (colors.length - 1), colors[i]);
    }

    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    const dataURL = canvas.toDataURL();

    return dataURL;
  }

  function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  function create_project() {
    let projectName = document.querySelector("#name").value;
    let projectDescription = document.querySelector("#description").value;

    const randomColors = [
      getRandomColor(),
      getRandomColor(),
      getRandomColor()
    ];
    const gradientURL = createGradientPictureURL(randomColors);

    const newProject = {
      id: generateRandomId(),
      name: projectName,
      description: projectDescription,
      image: gradientURL,
      link: '/project/acquisition',
      technologies: ['Svelte', 'JavaScript', 'HTML', 'CSS'],
      role: 'Facial Queues',
      created: '3 months'
    };


    projects.push(newProject);
    hasNewProjects = true;

    localStorage.setItem('projects', JSON.stringify(projects));

    // Close the modal
    const modal = document.querySelector("#newProject");
    const bootstrapModal = bootstrap.Modal.getInstance(modal);
    bootstrapModal.hide();

    console.log(projects);

    appendProjectCard(newProject);

    alert("Project created successfully!");
    // goToProjectLink(newProject.link + '?id=' + newProject.id);

  }

  function appendProjectCard(project) {
    const projectList = document.querySelector("#project_list");

    const projectCard = document.createElement("div");
    projectCard.classList.add("col");



    const cardBody = document.createElement("div");
    cardBody.classList.add("card-body", "p-0", "m-0");

    const row = document.createElement("div");
    row.classList.add("row", "mx-0", "h-100", "align-items-center");

    const imageColumn = document.createElement("div");
    imageColumn.classList.add("col-3", "m-0", "p-0", "h-100", "d-flex", "align-items-center");

    const image = document.createElement("img");
    image.src = project.image;
    image.alt = project.name;
    image.style.width = "100%";
    image.style.height = "100%";

    const contentColumn = document.createElement("div");
    contentColumn.classList.add("col-9", "p-3");

    const projectNameElement = document.createElement("h5");
    projectNameElement.textContent = project.name;

    const projectDescriptionElement = document.createElement("p");
    projectDescriptionElement.textContent = project.description;

    const projectButton = document.createElement("button");
    projectButton.classList.add("project-info-button");
    projectButton.style.height = "30px";
    projectButton.textContent = "Go to Project";
    projectButton.addEventListener("click", () => goToProject(project.link, project.id));

    const deleteButton = document.createElement("button");
    deleteButton.classList.add("delete-button");
    deleteButton.style.height = "30px";
    deleteButton.style.marginTop = "10px";
    deleteButton.textContent = "Delete";
    deleteButton.style.backgroundColor = "red";
    deleteButton.style.color = "white";
    deleteButton.style.border = "none";
    deleteButton.style.cursor = "pointer";
    deleteButton.style.marginLeft = "5px";
    deleteButton.addEventListener("click", (event) => {
      event.stopPropagation(); // Prevent event propagation
      deleteProject(projects.indexOf(project));
    });

    const cardContainer = document.createElement("div");
    cardContainer.classList.add("card", "h-100");
    cardContainer.style.cursor = "pointer";
    cardContainer.addEventListener("click", () => goToProject(project.link, project.id));

    cardContainer.appendChild(deleteButton);


    contentColumn.appendChild(projectNameElement);
    contentColumn.appendChild(projectDescriptionElement);
    contentColumn.appendChild(projectButton);
    contentColumn.appendChild(deleteButton);

    imageColumn.appendChild(image);

    row.appendChild(imageColumn);
    row.appendChild(contentColumn);

    cardBody.appendChild(row);

    cardContainer.appendChild(cardBody);

    projectCard.appendChild(cardContainer);

    projectList.appendChild(projectCard);

    // Adjust project cards layout
    adjustProjectCardsLayout();
  }

  function deleteProject(index) {
    if (confirm('Are you sure you want to delete this project?')) {
      projects.splice(index, 1);
      localStorage.setItem('projects', JSON.stringify(projects));
      adjustProjectCardsLayout();
      location.reload();
    }
  }

  function adjustProjectCardsLayout() {
    
    const projectCards = document.querySelectorAll('.card');
    const maxWidth = Math.max(...Array.from(projectCards).map((card) => card.offsetWidth));

    projectCards.forEach((card) => {
      card.style.width = `${maxWidth}px` - 5 + 'px';
    });

    
  }


  function goToProject(link, projectId) {
    console.log(link);
    window.location.href = (link + '?id=' + projectId);

  }
</script>




<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />


<div class="container py-4">
	<div class="d-flex">
		<div class="p-2 flex-grow-1">
			<h1>My Projects</h1>
      <button type="button" class="btn btn-light d-flex align-items-center" style="background-color: white; border-color: grey;" on:click={clearNewProjects} disabled={!hasNewProjects}>
        Clear New Projects
      </button>
        </div>
		<div class="p-2">
			<div class="input-group mb-3">
				<span class="input-group-text">New Project</span>
				<div class="form-floating">
					<button type="button" class="btn btn-light d-flex align-items-center" style="margin-left: auto;background-color: white; border-color: grey;" data-bs-toggle="modal" data-bs-target="#newProject">
            <span class="material-symbols-outlined">
              add
            </span>
				</div>
			</div>
		</div>
	</div>
    <div href="newProject" id="projectsHere" style="display:flex;">
              

         <div class="modal fade" id="newProject" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">

            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content" style="color: #292929">
                <div class="overlay"></div>
                <div class="modal-header">
                  <h5 class="modal-title">New Project</h5>
                  <button type="button" class="close" data-bs-dismiss="modal" onclick="window.location.href='/myprojects'" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <form>
                    <div class="form-group">
                      <label for="name">Name</label>
                      <input type="text" class="form-control" id="name" placeholder="Enter name">
                    </div>
                    <div class="form-group" style="margin-top: 10px;">
                      <label for="description">Description</label>
                      <textarea class="form-control" id="description" placeholder="Enter description"></textarea>
                    </div>
                   
                     <div class="row" style="margin-top: 10px;">
                        
                        <div class="col">
                          <div class="form-group" id="Privacy" value="Public">
                            <label for="option">Privacy</label>
                            <div class="form-check">
                              <input class="form-check-input" type="radio" name="privacy_option" value="public" checked>
                              <label class="form-check-label" for="public">
                                Public
                              </label>
                            </div>
                            <div class="form-check" >
                              <input class="form-check-input" type="radio" name="privacy_option" id="private" value="private">
                              <label class="form-check-label" for="private">
                                Private
                              </label>
                            </div>
                          </div>
                        </div>
                      </div>

                  </form>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-danger" data-bs-dismiss="modal" onclick="window.location.href='myprojects'">
                    <span class="material-symbols-outlined">
                      cancel
                      </span>
                </button>
                <button type="button" class="btn btn-success" on:click={() => create_project()}>
                  <span class="material-symbols-outlined">
                    save
                    </span>
                </button>
                </div>
            </div>
        </div>
         </div>
    </div>
        


        
    </div>

    <hr class="mbg-white border-3 opacity-100" style="border-color: #eee;">

  

    


    <div class="container">
      <div class="row row-cols-1 row-cols-md-3 g-4" id="project_list">
        {#each projects as project, index}
          <div class="col">
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <div class="card h-100" style="cursor:pointer;" on:click={() => goToProject(project.link, project.id)}>
              <div class="card-body p-0 m-0">
                <div class="row mx-0 h-100 align-items-center"> <!-- Added 'align-items-center' class -->
                  <div class="col-3 m-0 p-0 h-100 d-flex align-items-center"> <!-- Added 'd-flex' and 'align-items-center' classes -->
                    <img src={project.image} alt={project.name} style="width:100%; height:100%" />
                  </div>
                  <div class="col-9 p-3">
                    <h5>{project.name}</h5>
                    <p>{project.description}</p>
                    <button class="project-info-button" style="height: 30px" on:click={() => goToProject(project.link, project.id)}>
                      Go to Project
                    </button>
                    <button class="delete-button" style="height: 30px; margin-top: 10px" on:click={() => deleteProject(index)}>
                      Delete
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        {/each}
      </div>
    </div>
    
    


