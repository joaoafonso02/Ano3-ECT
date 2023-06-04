<script lang="ts">
	import { onMount } from 'svelte';

	let videoDiv: HTMLDivElement;
	let webVideo : HTMLVideoElement;
	let canva1: HTMLCanvasElement;
	let canva2: HTMLCanvasElement;
	let width: number, height: string;

	let stream;
	let isPlaying: boolean = false;

	let checkboxs: Object[] = [];
	
	onMount( async () => {
		videoDiv.style.height = width * (3/4) + "px";

		load()
		
	})

	async function load() {
		const response = await fetch('http://localhost:5000/api/feature');
		const data: string[] = await response.json();
		const dataParsed: Array<Object> = data.map((elem,i)=>{
			return {
				"name": elem.split("_").join(" ").toUpperCase(),
				"code": elem,
				"points": [],
				"edges": [],
				"elem": false
			}
		})
		checkboxs = dataParsed;
	} 
	

	async function openCamera() {
		try {
			stream = await navigator.mediaDevices.getUserMedia({ video: true }); // only video no audio
		} catch (error) {
			console.error('Error opening camera:', error);
			return;
		}

		webVideo.srcObject = stream;
		isPlaying = true;

		// prepare canvas
		let ctx = canva1.getContext('2d');
		let ctxPoints: CanvasRenderingContext2D = canva2.getContext('2d');
		ctxPoints.fillStyle = "#FF0000";
		let cw = canva2.width, ch = canva2.height;

		var runnnig = false;
		let intervel = setInterval( async ()=>{
			if( runnnig ) return;
			runnnig = true;
			ctx?.drawImage(webVideo, 0, 0, cw, ch);
			

			for(let checkbox of checkboxs) {
				if( !checkbox.elem ) continue;
				let blob: Blob = await new Promise(resolve => canva1.toBlob(resolve, 'image/png'));
				let form = new FormData();
				form.append('blob', blob);
				let response = await fetch('http://localhost:5000/api/feature/'+checkbox.code, {
					method: 'POST',
					body: form
				})
				ctxPoints.clearRect(0, 0, cw, ch);
				response = await response.json();
				console.log(response)
				if( !response.status ) break;
				for(let j=0; j<response.points.length; j++) {
					for(let point of response.points[j].edges) {
						ctxPoints?.beginPath();
						ctxPoints?.moveTo(response.points[j].vertices[point[0]].x*cw, response.points[j].vertices[point[0]].y*ch);
						ctxPoints?.lineTo(response.points[j].vertices[point[1]].x*cw, response.points[j].vertices[point[1]].y*ch);
						ctxPoints?.stroke();
					}
					for(let point of response.points[j].vertices) {
						ctxPoints.beginPath();
						ctxPoints.arc(point.x*cw, point.y*ch, 2, 0, 2 * Math.PI);
						ctxPoints.fill();
					}
				}
			}
			runnnig = false;

			
		}, 1000/30);
		
	}
</script>

<div class="row">
	<div class="col-3" style="margin-right: 100px;">
		<h5 class="my-4">Media Pipe Feature Calculator</h5>
		<form>
			<fieldset>
				{#each checkboxs as checkbox}
					<div class="input-group">
						<div class="input-group-text">
							<input
								id={"check"+checkbox.name}
								class="form-check-input mt-0"
								type="checkbox"
								bind:checked={checkbox.elem}
								aria-label="Checkbox for following text input"
							/>
						</div>
						<span class="input-group-text" style="flex-grow: 1;">{checkbox.name}</span>
					</div>
				{/each}
				<!-- <div class="input-group">
					<div class="input-group-text">
						<input
							class="form-check-input mt-0"
							type="checkbox"
							value=""
							aria-label="Checkbox for following text input"
						/>
					</div>
					<span class="input-group-text" style="flex-grow: 1;">MediaPipe - Hand Gesture</span>
				</div>

				<div class="input-group">
					<div class="input-group-text">
						<input
							class="form-check-input mt-0"
							type="checkbox"
							value=""
							aria-label="Checkbox for following text input"
						/>
					</div>
					<span class="input-group-text" style="flex-grow: 1;">MediaPipe - Pose Detection</span>
				</div>

				<div class="input-group">
					<div class="input-group-text">
						<input
							class="form-check-input mt-0"
							type="checkbox"
							value=""
							aria-label="Checkbox for following text input"
						/>
					</div>
					<span class="input-group-text" style="flex-grow: 1;">MediaPipe - Holistic Detection</span>
				</div> -->
			</fieldset>
		</form>

		<!-- {#if !isPlaying} -->
			<button
				class="btn btn-dark w-100 text-center mt-2"
				id="record"
				type="submit"
				on:click={openCamera}
			>
				{#if !isPlaying}
					Open Camera
				{:else}
					Close Camera
				{/if}
			</button
			>
	</div>
	<div bind:this={videoDiv} class="col-8 bg-dark p-0" bind:offsetWidth={width}>
		<div class="icon-container w-100 h-100 p-0">
			<video
				class="w-100 h-100"
				bind:this={webVideo}
				autoplay
				muted
			/>
		</div>
		<canvas class="w-100 h-100" bind:this={canva1} style="display:none;width:500px;height:500px;"></canvas>
		<canvas class="w-100 h-100" bind:this={canva2} style="position:absolute;width:50px;height:50px;top:0;"></canvas>
		<p style="text-align:center">
			Guessed Class: Thumbsup <br />
			Accuracy: 0.89
		</p>
	</div>
</div>

<style>
	/* .icon-container {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.icon {
		display: block;
		margin: auto;
		max-width: 10%;
		max-height: 10%;
	} */
</style>
