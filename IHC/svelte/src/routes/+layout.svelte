<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	let body: HTMLElement;	
	let nav: HTMLElement;
	let footer: HTMLElement;
	let container: HTMLElement;

	onMount( () => {
		container.style.minHeight = (window.innerHeight-footer.offsetHeight-nav.offsetHeight)+'px';
	})

	let path: string;
	$: path = $page.url.pathname;
</script>

<div class="" bind:this={body}>

	<nav class="navbar navbar-expand-lg bg-body-tertiary" bind:this={nav}>

		<div class="container">
			<a class="navbar-brand" href="/">MFDAA</a>
			<button
				class="navbar-toggler"
				type="button"
				data-bs-toggle="collapse"
				data-bs-target="#navbarSupportedContent"
				aria-controls="navbarSupportedContent"
				aria-expanded="false"
				aria-label="Toggle navigation"
			>
				<span class="navbar-toggler-icon" />
			</button>
			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav me-auto mb-2 mb-lg-0">
					<li class="nav-item">
						<a class="nav-link {path == '/community' ? 'active' : ''}" href="/community">Community</a>
					</li>
					<li class="nav-item">
						<a class="nav-link {path == '/myprojects' ? 'active' : ''}" href="/myprojects"
							>MyProjects</a
						>
					</li>
				</ul>
				<ul class="navbar-nav">
					<li class="nav-link">
						<a class="nav-link {path == '/browse' ? 'active' : ''}" href="/profile">Profile</a>
					</li>
					<li class="nav-link">
						<a class="nav-link {path == '/browse' ? 'active' : ''}" href="/login">Login/Register</a
						>
					</li>
				</ul>
			</div>
		</div>
	</nav>

	<div class="container" bind:this={container}>
		<slot />
	</div>

	<footer class="bg-dark text-center text-white" style="" bind:this={footer}>
		<div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">© 2023 MFDAA</div>
	</footer>
</div>

<style>
	/* footer {
		position: absolute;
		bottom: 0;
		width: 100%;
	} */
</style>
