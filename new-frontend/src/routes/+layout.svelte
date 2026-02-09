<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
	
</script>

<svelte:head><link rel="icon" href={favicon} />
	<script>
    	document.documentElement.setAttribute('data-theme', 'dark');
	</script>
</svelte:head>
{@render children()}
