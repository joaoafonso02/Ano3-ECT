<link rel="stylesheet" href="src/routes/myprojects/styles.css">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />


<div class="container my-2" style="margin-top:100px"> 
	<br>
	<h2 style="text-align:center;color: black">Your Profile 
		<span class="material-icons" style="cursor: pointer;font-size: 1.5rem;" on:click={editProfile}>edit</span>
	</h2>

	<div style="text-align:center;margin-top:20px"class="container">
		<div class="row justify-content-center">
			<div class="card-client">
				<div class="user-picture">
					<img src="/veloso.jpg" alt="vitruviano" style="width:100%;height:100%;" />
				</div>
				<p class="name-client">
					<span id="name-container">Rui Veloso</span><br>
					<span id="occupation-container">Engineering Student</span><br>
					<span id="email-container"><b>Email:</b> anelderubi@gmail.com</span><br>
					<span id="contact-container"><b>Contact:</b> +351 912 345 678</span><br>
					<span id="country-container"><b>Country:</b> Portugal</span><br>
					<a href=""><u>Change Password</u></a>
				</p>
				<br>
				<div class="social-media">
					<a href="#">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
							<path d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"></path>
						</svg>
						<span class="tooltip-social">Twitter</span>
					</a>
					<a href="#">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
							<path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"></path>
						</svg>
						<span class="tooltip-social">Instagram</span>
					</a>
					<a href="#">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
							<path d="M504 256C504 119 393 8 256 8S8 119 8 256c0 123.78 90.69 226.38 209.25 245V327.69h-63V256h63v-54.64c0-62.15 37-96.48 93.67-96.48 27.14 0 55.52 4.84 55.52 4.84v61h-31.28c-30.8 0-40.41 19.12-40.41 38.73V256h68.78l-11 71.69h-57.78V501C413.31 482.38 504 379.78 504 256z"></path>
						</svg>
						<span class="tooltip-social">Facebook</span>
					</a>
					<a href="#">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
							<path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"></path>
						</svg>
						<span class="tooltip-social">LinkedIn</span>
					</a>
				</div>
			</div>
		</div>  
	</div>
</div>

<br>

<div style="text-align: center;">
	<button class="btn btn-danger" style="background-color: #121212;opacity:0.5; border-color: #343335; margin-right: 20px; width: 150px;"><a style="color: #e0e2d7; border-color: #343335;"href="/myprojects">My Projects</a></button>
	<button class="btn btn-danger" style="background-color: #ff3333; border-color: #cc0000;" data-bs-toggle="modal" data-bs-target="#deleteModal"><a style="color: #e0e2d7;" >Delete Account</a></button>


		<div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true" >
			<div class="modal-dialog">
				<div class="modal-content" >
				<div class="modal-header">
					<h5 class="modal-title" id="deleteModalLabel">Delete Account</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<p style="text-align:left">Are you sure you want to delete your account permanently?</p>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
					<button type="button" class="btn btn-danger" on:click={deleteAccount}>Delete</button>
				</div>
			</div>
		</div>


	</div>
</div>

<script>
	function deleteAccount() {
	  // Delete account logic here
	  
	  // Show alert after deleting account
	  alert("Your account has been deleted!");
	  
	  // Redirect to home page
	  window.location.href = "/";
	}
	
	import { onMount } from 'svelte';

	onMount(() => {
		const nameContainer = document.getElementById('name-container');
		const occupationContainer = document.getElementById('occupation-container');
		const emailContainer = document.getElementById('email-container');
		const contactContainer = document.getElementById('contact-container');
		const countryContainer = document.getElementById('country-container');

		// Retrieve values from local storage
		const name = localStorage.getItem('name');
		const occupation = localStorage.getItem('occupation');
		const email = localStorage.getItem('email');
		const contact = localStorage.getItem('contact');
		const country = localStorage.getItem('country');

		// Update the containers with the saved values
		nameContainer.innerHTML = name;
		occupationContainer.innerHTML = occupation;
		emailContainer.innerHTML = '<b>Email:</b> ' + email;
		contactContainer.innerHTML = '<b>Contact:</b> ' + contact;
		countryContainer.innerHTML = '<b>Country:</b> ' + country;
	});

	
	function editProfile() {
		var nameContainer = document.getElementById('name-container');
		var occupationContainer = document.getElementById('occupation-container');
		var emailContainer = document.getElementById('email-container');
		var contactContainer = document.getElementById('contact-container');
		var countryContainer = document.getElementById('country-container');

		// Check if inputs already exist
		if (!nameContainer.querySelector('input')) {
			// Inputs don't exist, create them with saved values from local storage
			var nameInput = document.createElement('input');
			var occupationInput = document.createElement('input');
			var emailInput = document.createElement('input');
			var contactInput = document.createElement('input');
			var countryInput = document.createElement('input');

			nameInput.value = nameContainer.textContent.trim();
			occupationInput.value = occupationContainer.textContent.trim();
			emailInput.value = emailContainer.textContent.trim().replace('Email: ', '');
			contactInput.value = contactContainer.textContent.trim().replace('Contact: ', '');
			countryInput.value = countryContainer.textContent.trim().replace('Country: ', '');

			nameContainer.innerHTML = '';
			nameContainer.appendChild(nameInput);

			occupationContainer.innerHTML = '';
			occupationContainer.appendChild(occupationInput);

			emailContainer.innerHTML = '';
			emailContainer.appendChild(emailInput);

			contactContainer.innerHTML = '';
			contactContainer.appendChild(contactInput);

			countryContainer.innerHTML = '';
			countryContainer.appendChild(countryInput);
		} else {
			// Inputs already exist, save changes to local storage
			var nameInput = nameContainer.querySelector('input');
			var occupationInput = occupationContainer.querySelector('input');
			var emailInput = emailContainer.querySelector('input');
			var contactInput = contactContainer.querySelector('input');
			var countryInput = countryContainer.querySelector('input');

			localStorage.setItem('name', nameInput.value);
			localStorage.setItem('occupation', occupationInput.value);
			localStorage.setItem('email', emailInput.value);
			localStorage.setItem('contact', contactInput.value);
			localStorage.setItem('country', countryInput.value);

			// Replace the inputs with updated text
			nameContainer.innerHTML = localStorage.getItem('name');
			occupationContainer.innerHTML = localStorage.getItem('occupation');
			emailContainer.innerHTML = '<b>Email:</b> ' + localStorage.getItem('email');
			contactContainer.innerHTML = '<b>Contact:</b> ' + localStorage.getItem('contact');
			countryContainer.innerHTML = '<b>Country:</b> ' + localStorage.getItem('country');
		}
	}
</script>

<style>
	
	/* profile page: */
	.card-client {
	margin-top: 15px;
	background: white;
	width: 24rem;
	height: 41rem;
	padding-top: 25px;
	padding-bottom: 25px;
	padding-left: 20px;
	padding-right: 20px;
	border: 1px solid black;
	box-shadow: 0 6px 10px rgba(207, 212, 222, 1);
	border-radius: 10px;
	text-align: center;
	color: black;
	font-family: "Poppins", sans-serif;
	transition: all 0.3s ease;
	}

	.card-client:hover {
	transform: translateY(-10px);
	}

	.user-picture {
	overflow: hidden;
	object-fit: cover;
	width: 12rem;
	height: 12rem;
	border: 1px solid black;
	border-radius: 999px;
	display: flex;
	justify-content: center;
	align-items: center;
	margin: auto;
	}

	.user-picture svg {
	width: 2.5rem;
	fill: currentColor;
	}

	.name-client {
	margin: 0;
	margin-top: 20px;
	font-weight: 600;
	font-size: 18px;
	}

	.name-client span {
	display: block;
	font-weight: 200;
	font-size: 16px;
	}

	.social-media:before {
	content: " ";
	display: block;
	width: 100%;
	height: 2px;
	margin: 20px 0;
	background: #61554d;
	}

	.social-media a {
	position: relative;
	margin-right: 15px;
	text-decoration: none;
	color: inherit;
	}

	.social-media a:last-child {
	margin-right: 0;
	}

	.social-media a svg {
	width: 1.1rem;
	fill: currentColor;
	}

	/*-- Tooltip Social Media --*/
	.tooltip-social {
	background: #eee;
	display: block;
	position: absolute;
	bottom: 0;
	left: 50%;
	padding: 0.5rem 0.4rem;
	border-radius: 5px;
	font-size: 0.8rem;
	font-weight: 600;
	opacity: 0;
	pointer-events: none;
	transform: translate(-50%, -90%);
	transition: all 0.2s ease;
	z-index: 1;
	}

	.tooltip-social:after {
	content: " ";
	position: absolute;
	bottom: 1px;
	left: 50%;
	border: solid;
	border-width: 10px 10px 0 10px;
	border-color: transparent;
	transform: translate(-50%, 100%);
	}

	.social-media a .tooltip-social:after {
	border-top-color: #eee;
	}

	.social-media a:hover .tooltip-social {
	opacity: 1;
	transform: translate(-50%, -130%);
	}


	
	img {
	display: block;
	width: 100%;
	max-width: 1500px;
	/* rounded corners */
	border-radius: 10px;
	}



</style>