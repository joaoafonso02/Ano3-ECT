<script lang='ts'>
  let width: number, height: string;

  let records = [
  ];

  function editName(id) {
    const record = records.find(r => r.id === id);
    record.editingName = true;
  }

  import { onMount } from 'svelte';

  onMount(() => {

    // localStorage.clear();
    loadRecords();

  });
    
  let stream;
  let recorder;
  let chunks = [];
  let isPlaying = false;
  let isRecording = false;
  let countDown = 0;
  let duration = 0;
  


  function closeModal() {
    const modal = document.getElementById('previewVideoModal');
    const bootstrapModal = bootstrap.Modal.getInstance(modal);
    bootstrapModal.hide();

    // force close modal
    bootstrapModal.hide();

    document.body.classList.remove('modal-open');
    document.body.style.overflow = ''; // Restore scrolling

 
    console.log('close modal');
  }



  let isCameraOn = false; // flag to keep track of camera state
  
  function loadRecords() {
    const storedRecords = localStorage.getItem('records');

    if (storedRecords) {
      records = JSON.parse(storedRecords);
    }
  }


  async function openCamera() {
    try {
      if (isCameraOn) {
        // Camera is already on, so turn it off
        stopCamera();
        return;
      }

      // Request camera access
      stream = await navigator.mediaDevices.getUserMedia({ video: true }); // only video, no audio
      const videoElement = document.querySelector('video');

      let videoPositon = document.getElementById('icon.container');

      videoElement.srcObject = stream; 

      recorder = new MediaRecorder(stream);

      // make the video over videoposition
      videoElement.style.position = 'absolute';
      videoElement.style.top = '0px';
      videoElement.style.left = '0px';
      videoElement.style.width = '100%';
      videoElement.style.height = '100%';
      videoElement.style.objectFit = 'cover';
      



      recorder.addEventListener('dataavailable', event => {
        chunks.push(event.data);
        console.log(chunks);
      });

      const closeCamera = document.getElementById('openCamera');
      closeCamera.innerHTML = 'Close Camera';

      isCameraOn = true; // Set the camera state to on

    } catch (error) {
      console.error('Error opening camera:', error);
    }
  }

  function stopCamera() {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      stream = null;
    }
    const videoElement = document.querySelector('video');
    if (videoElement) {
      videoElement.srcObject = null;
    }
    const bgBlackElement = document.querySelector('.bg-black');
    if (bgBlackElement) {
      
      bgBlackElement.style.display = 'block';
    }

    const closeCamera = document.getElementById('openCamera');
    closeCamera.innerHTML = 'Open Camera';

    isCameraOn = false; // Set the camera state to off
  }



  async function startRecording() {
    isRecording = true;
    
    const startRecord = document.getElementById('record');
    startRecord.style.display = 'none';

    if (recorder && recorder.state === 'inactive') { // if cam is open, start recording
      countDown = parseInt(document.getElementById('count-down-input').value);
      duration = parseInt(document.getElementById('duration-input').value);

      const countDownText = document.getElementById('count-down-text');
      const recordingText = document.getElementById('recording-text');
      countDownText.innerHTML = countDown;

      const intervalId = setInterval(() => {
        countDown--;
        countDownText.innerHTML = countDown;
        if (countDown <= 0) {
          clearInterval(intervalId);
          countDownText.style.display = "none";

          try {
            recordingText.innerHTML = "Recording...";
            recorder.start(100);
            console.log('Recording video ...');

            setTimeout(() => {
              stopRecording();
              recordingText.innerHTML = "";
            }, duration * 1000);
          } catch (error) {
            console.error('Error starting recording:', error);
          }
        }
      }, 1000);
    }
}

async function stopRecording() {
  if (recorder && recorder.state === 'recording') {
    recorder.stop();
    isRecording = false;
    console.log('Stopped recording video.');
    const stopEventListener = () => {
      recorder.removeEventListener('stop', stopEventListener); // Remove the event listener
      previewVideo();
      // if (confirm('Do you want to download the video?')) {
      //   downloadVideo();
      // }
    };
    recorder.addEventListener('stop', stopEventListener);
  }
}

function previewVideo() {
  const modalVideo = document.getElementById('previewVideo');
  const blob = new Blob(chunks, { type: 'video/webm' });
  const videoURL = URL.createObjectURL(blob);
  console.log(videoURL)

  modalVideo.src = videoURL;

  const modal = new bootstrap.Modal(document.getElementById('previewVideoModal'));
  modal.show();

  const downloadButton = document.getElementById('download-button');
  downloadButton.removeEventListener('click', downloadVideo);

  // Prompt for filename before calling downloadVideo
  const filename = prompt('Enter a name for the video file:', 'recorded-video');
  if (filename) {
    downloadButton.addEventListener('click', () => downloadVideo(videoURL, filename));
  }

  const closeModalButton = document.querySelector('#previewVideoModal .btn-close');
  closeModalButton.removeEventListener('click', () => closeModal(modal));

  const startRecord = document.getElementById('record');
  startRecord.style.display = 'block';
}

function downloadVideo(url, filename) {
  const a = document.createElement('a');
  document.body.appendChild(a);
  a.style = 'display: none';
  a.href = url;
  a.download = filename + '.webm';
  //a.click();
  window.URL.revokeObjectURL(url);

  chunks = [];

  let newRecordClass = document.getElementById('inputGroupSelect02').value;

  let newRecordid = records.length + 1;

  const newRecord = {
    id: newRecordid,
    name: filename,
    class: newRecordClass,
    duration: duration,
    url: url
  };

  records.push(newRecord);

  localStorage.setItem('records', JSON.stringify(records));

  closeModal();
  renderRecords();
}

  function renderRecords() {
    const tableBody = document.querySelector('tbody');
    tableBody.innerHTML = ''; // Clear the existing rows

    // create an array to store the records that are already listed on the table
    const recordsOnTable = [];

    for (const record of records) { 
      const tableRow = document.createElement('tr');
      tableRow.setAttribute('id', `record-${record.id}`);

      const idCell = document.createElement('th');
      idCell.setAttribute('scope', 'row');
      idCell.textContent = record.id;
      tableRow.appendChild(idCell);

      const nameCell = document.createElement('td');
      nameCell.id = `recordName-${record.id}`;
      const nameText = document.createElement('span');
      nameText.textContent = record.name;
      nameCell.appendChild(nameText);
      tableRow.appendChild(nameCell);

      const classCell = document.createElement('td');
      classCell.id = `recordClass-${record.id}`;

      const classText = document.createElement('span');
      classText.textContent = record.class;
      classCell.appendChild(classText);
      tableRow.appendChild(classCell);

      const durationCell = document.createElement('td');
      durationCell.textContent = record.duration;
      tableRow.appendChild(durationCell);

      const actionsCell = document.createElement('td');
      const deleteButton = document.createElement('button');
      deleteButton.setAttribute('class', 'btn btn-danger');
      deleteButton.addEventListener('click', () => deleteRecord(record.id));
      const deleteIcon = document.createElement('i');
      deleteIcon.setAttribute('class', 'fas fa-trash');
      deleteButton.style.marginRight = '5px';
      deleteButton.style.marginLeft = '50px';
      deleteButton.appendChild(deleteIcon);
      deleteButton.setAttribute('title', 'Delete Video');

      const editButton = document.createElement('button');
      editButton.setAttribute('class', 'btn btn-dark');
      editButton.addEventListener('click', () => editRecord(record.id));
      const editIcon = document.createElement('i');
      editIcon.setAttribute('class', 'fas fa-edit');
      editButton.style.marginRight = '5px';
      editButton.appendChild(editIcon);
      editButton.setAttribute('title', 'Edit Video Elements');

      const previewCell = document.createElement('td');
      const previewButton = document.createElement('button');
      previewButton.setAttribute('class', 'btn btn-dark');
      previewButton.addEventListener('click', () => previewRecord(record.id));
      const previewIcon = document.createElement('i');
      previewIcon.setAttribute('class', 'fas fa-eye');
      previewButton.style.marginRight = '5px';
      previewButton.appendChild(previewIcon);
      previewButton.setAttribute('title', 'Preview Video');

      actionsCell.appendChild(deleteButton);
      actionsCell.appendChild(editButton);
      actionsCell.appendChild(previewButton);
      
      tableRow.appendChild(actionsCell);
      tableBody.appendChild(tableRow);

      recordsOnTable.push(record.id);
      console.log(recordsOnTable)
    
      if(record.name == 'undefined'){
        deleteRecord(record.id); 
      } 

    }
    localStorage.setItem('records', JSON.stringify(records));
  }

  

  function deleteRecord(id) {
    const index = records.findIndex(record => record.id === id);

    if (index !== -1) {
      records.splice(index, 1);
      localStorage.setItem('records', JSON.stringify(records));
      renderRecords(); // Update the table display
    }
  }


  function previewRecord(id) {
    const record = records.find(r => r.id === id);
    const videoURL = record.url;

    const modalVideo = document.getElementById('previewVideo');
    modalVideo.src = videoURL;

    const modal = new bootstrap.Modal(document.getElementById('previewVideoModal'));
    modal.show();

    const downloadButton = document.getElementById('download-button');
    downloadButton.removeEventListener('click', downloadVideo);
    downloadButton.addEventListener('click', () => downloadVideo(videoURL));

    const closeModalButton = document.querySelector('#previewVideoModal .btn-close');
    closeModalButton.removeEventListener('click', closeModal);
    closeModalButton.addEventListener('click', () => closeModal(modal));

    const startRecord = document.getElementById('record');
    startRecord.style.display = 'block';
  }


  function editRecord(id) {
    const record = records.find(r => r.id === id);

    var nameContainer = document.getElementById(`recordName-${id}`);

    if (!nameContainer.querySelector('input')) {
      // Convert name cell to input element
      const nameCell = document.getElementById(`recordName-${id}`);
      const nameInput = document.createElement('input');
      nameInput.type = 'text';
      nameInput.value = record.name;
      nameInput.id = `name-input-${id}`; // Add ID to name input
      nameCell.innerHTML = '';
      nameCell.appendChild(nameInput);

      // Convert class cell to select element
      const classCell = document.getElementById(`recordClass-${id}`);
      const classSelect = document.createElement('select');
      classSelect.id = `recordClassSelect-${id}`;

      const thumbsUpOption = document.createElement('option');
      thumbsUpOption.value = 'ThumbsUp';
      thumbsUpOption.textContent = 'ThumbsUp';
      classSelect.appendChild(thumbsUpOption);

      const thumbsDownOption = document.createElement('option');
      thumbsDownOption.value = 'ThumbsDown';
      thumbsDownOption.textContent = 'ThumbsDown';
      classSelect.appendChild(thumbsDownOption);

      const peaceSignOption = document.createElement('option');
      peaceSignOption.value = 'PeaceSign';
      peaceSignOption.textContent = 'Peace';
      classSelect.appendChild(peaceSignOption);

      classSelect.value = record.class;
      classCell.innerHTML = '';
      classCell.appendChild(classSelect);
    } else {
      // Convert name input to text
      const nameInput = document.getElementById(`name-input-${id}`);
      record.name = nameInput.value;
      const nameCell = document.getElementById(`recordName-${id}`);
      nameCell.innerHTML = '';
      const nameText = document.createElement('span');
      nameText.textContent = record.name;
      nameCell.appendChild(nameText);

      // Convert class select to text
      const classSelect = document.getElementById(`recordClassSelect-${id}`);
      record.class = classSelect.value;
      const classCell = document.getElementById(`recordClass-${id}`);

      classCell.innerHTML = '';
      const classText = document.createElement('span');
      classText.textContent = record.class;
      classCell.appendChild(classText);

      // Save them in local storage
      localStorage.setItem('records', JSON.stringify(records));
    }

    localStorage.setItem('records', JSON.stringify(records));
  }



  $: height = (width*(3/4)) + 'px';


</script>

<div class="row">
	<div class="col-3"  style="margin-right: 100px;">
		<form>
			<fieldset>
        <h5 class="my-4">Options:</h5>
				<div class="input-group">
					<select class="form-select" id="inputGroupSelect02">
						<option selected>ThumbsUp</option>
						<option>ThumbsDown</option>
						<option>Peace</option>
					</select>
					<button class="btn btn-dark input-group-text">+</button>
				</div>
				<div class="input-group">
          <span class="input-group-text w-75">Count Down</span>
          <input type="number" aria-label="First name" class="form-control" value="1" id="count-down-input"/>
        </div>
        <div class="input-group">
          <span class="input-group-text w-75">Duration</span>
          <input type="number" aria-label="First name" class="form-control" value="1" id="duration-input"/>
        </div>
        {#if !isPlaying}
        <button id="openCamera" type="submit" class="btn btn-dark w-100 text-center mt-2" on:click={openCamera}>Open Camera</button>
        {/if} 
				<button id="record" type="submit" class="btn btn-dark w-100 text-center mt-2" on:click={startRecording}>Record</button>
       
  
        <br>
        <p id="count-down-text" style="text-align:center"></p>
        <p id="recording-text" style="text-align:center"></p>
	    </fieldset>
		</form>
	</div>

	<div class="col-8 bg-dark" style="height:{height}" bind:offsetWidth={width}>
    <div class="icon-container">
        <video width="2640" height="480" style="height:{height}" bind:offsetWidth={width} autoplay muted></video>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        {#if !isPlaying}
          <!-- <img id="play" src="/src/routes/img/play.png" alt="Icon" class="icon" style="" on:click={openCamera}>

            <button id="play" class="icon" style="display: flex; justify-content: center; align-items: center;margin-right:880px;margin-top:170px;" on:click={openCamera}>Start Camera</button> -->
        {:else}
          <!-- <img id="pause" src="/src/routes/img/stop.png" alt="Icon" class="icon" style="display: flex; justify-content: center; align-items: center;" on:click={stopCamera}> -->
        {/if} </div>
    </div>
  </div>
  
 
  <div class="modal" id="previewVideoModal">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Preview Video</h5>
          <button type="button" class="btn-close" on:click={() => closeModal()} aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <video id="previewVideo" controls class="w-100" autoplay>
            <track kind="captions" />
          </video>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" id="download-button"> Save & Download Video</button>
        </div>
      </div>
    </div>
  </div>
  

<hr class="my-4">

<div class="row mb-5">
  <h1>Records</h1>
  <table class="table" style="text-align:center">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Class</th>
        <th scope="col">Duration (s)</th>
      </tr>
    </thead>
    <tbody>
      {#each records as record (record.id)}
        <tr id="record-{record.id}">
          <th scope="row">{record.id}</th>
          <td id="recordName-{record.id}">{record.name}</td>
          <td id="recordClass-{record.id}">{record.class}</td>
          <td>{record.duration}</td>
          <td>
            <button class="btn btn-danger" on:click={() => deleteRecord(record.id)}>
              <i class="fas fa-trash"></i>
            </button>
            <button class="btn btn-dark" on:click={() => editRecord(record.id)}>
              <i class="fas fa-edit"></i>
            </button>
            <button class="btn btn-dark" on:click={() => previewRecord(record.id)}>
              <i class="fas fa-eye"></i>
            </button>
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>


<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<style>
   

  #play {
    display: block;
    max-width: 10%;
    max-height: 10%;
  }

  #pause {
    display: block;
    margin: auto;
    max-width: 6.5%;
    max-height: 6.5%;
  }
  
  #previewVideo {
    max-width: 100%;
    max-height: 60vh;
  }


</style>