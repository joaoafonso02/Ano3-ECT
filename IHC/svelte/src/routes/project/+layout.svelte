
<script lang="ts">
    import { page } from '$app/stores';
    
    let path: string;

    $: path = $page.url.pathname;

    import { onMount } from 'svelte';

    let message = "";

    onMount(() => {
    showAlert("Start by opening the camera if you wish to start recording!");
    });

    function showAlert(msg) {
        message = msg;
    }


</script>


{#if message}
<div class="alert">{message}</div>
{/if}
<nav class="nav py-4 nav-pills flex-column flex-sm-row">
    <a class="flex-sm-fill text-sm-center nav-link {path=='/project/acquisition'?'active':''}" href="acquisition">Acquisition</a>
    <a class="flex-sm-fill text-sm-center nav-link {path=='/project/test'?'active':''}" href="test">Test</a>
</nav>

<slot />

<style>
    nav a {
        background-color: #eee;
    }
    nav .active {
        background-color: black;
        color: white;
    }
    .nav-link {
        color: black;
    }

    .alert {
        background-color: #eee;
        color: black;
        text-align: center;
        padding: 10px;
        margin-top: 10px;
    }

</style>