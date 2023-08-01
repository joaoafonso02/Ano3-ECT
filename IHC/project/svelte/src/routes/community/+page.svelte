<link rel="stylesheet" href="src/routes/myprojects/styles.css">

<div class="container py-4">
	<div class="d-flex my-4">
		<div class="p-2 w-100">
			<h1>Community Projects</h1>
		</div>
		<div class="p-2 input-group my-1" style="width:500px;">
			<span class="input-group-text" id="basic-addon1">
				<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
					<path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
				  </svg>
			</span>
			<input type="text" class="form-control" placeholder="search" />
		</div>
	</div>
	<hr class="mbg-white border-3 opacity-100" style="border-color: #eee;">

	<div class="">
		<div class="row row-cols-1 row-cols-md-3 g-4">
			<div class="col">
				<div class="card h-100" style="cursor:pointer;" on:click={()=>window.location.href='/project/acquisition'}>
					<div class="card-body p-0 m-0">
						<div class="row mx-0 h-100">
							<div class="col-3 m-0 p-0 h-100">
								<img
									src="/communityhand.jpeg"
									alt="communityhand"
									style="width:100%;height:100%;"
								/>
							</div>
							<div class="col-9 p-3">
								<h5 class="card-title">Hand Gestures</h5>
								<p class="card-text">
									Here you can find and see all of the data sets created until today
								</p>
								<button class="project-info-button" style="height: 30px" on:click={()=>window.location.href='/project/acquisition'}>
									Go to Project
								  </button>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="col">
				<div class="card h-100" style="cursor:pointer;" on:click={()=>window.location.href='/project/acquisition'}>
					<div class="card-body p-0 m-0">
						<div class="row mx-0 h-100">
							<div class="col-3 m-0 p-0 h-100">
								<img
									src="/communityface.jpeg"
									alt="communityface"
									style="width:100%;height:100%;"
								/>
							</div>
							<div class="col-9 p-3">
								<h5 class="card-title">Facial Queues</h5>
								<p class="card-text">
									When you can record or upload your own videos to create a new dataset
								</p>
								<button class="project-info-button" style="height: 30px" on:click={()=>window.location.href='/project/acquisition'}>
									Go to Project
								  </button>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="col">
				<div class="card h-100" style="cursor:pointer;" on:click={()=>window.location.href='/project/acquisition'}>
					<div class="card-body p-0 m-0">
						<div class="row mx-0 h-100">
							<div class="col-3 m-0 p-0 h-100">
								<img src="/vitruviano.jpeg" alt="vitruviano" style="width:100%;height:100%;" />
							</div>
							<div class="col-9 p-3">
								<h5 class="card-title">Body Language</h5>
								<p class="card-text">
									Here you can find and see all of the data sets created until today
								</p>
								<button class="project-info-button" style="height: 30px" on:click={()=>window.location.href='/project/acquisition'}>
									Go to Project
								  </button>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="col">
				<div class="card h-100" style="cursor:pointer;" on:click={()=>window.location.href='/project/acquisition'}>
					<div class="card-body p-0 m-0">
						<div class="row mx-0 h-100">
							<div class="col-3 m-0 p-0 h-100">
								<img src="/travishair.jpeg" alt="travishair" style="width:100%;height:100%;" />
							</div>
							<div class="col-9 p-3">
								<h5 class="card-title">Travis The One</h5>
								<p class="card-text">
									At the video acquisition the user can label and annotate their own videos at his
									free will
								</p>
								<button class="project-info-button" style="height: 30px" on:click={()=>window.location.href='/project/acquisition'}>
									Go to Project
								  </button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>


