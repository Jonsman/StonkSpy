<section class="mainSection"
        class:logo-launch={logoLaunched}
        class:logo-return={!logoLaunched}
        style={`--logo-transform-y: ${logoTransformY}`}>
    <img
        class="logo"
        src={logo}
        alt="StonkSpy is nice"
        on:click={launchLogo}
    />
    <div>
        <input class="searchBar rounded-2xl focus:outline-2 focus:outline-offset-2"
        placeholder="Tolle Suche hier..."
        on:keydown={
            (e) => {
                if (e.key === 'Enter') {
                    onSearch((e.currentTarget as HTMLInputElement).value)
                }
            }
        }>
    </div>
</section>

<style>
    .mainSection {
        justify-items: center;
    }
    .logo {
        min-width: min(480px, 10vh);
        padding-bottom: 16px;
    }
    .searchBar {
        min-width: max(640px, 30vh);
        color: var(--text);
        background-color: color-mix(in srgb, var(--bg) 90%, var(--text) 10%);
        border: solid 1px;
        border-color: color-mix(in srgb, var(--accent) 25%, transparent);
    }
    .searchBar:placeholder {
        color: color-mix(in rgb, var(--bg) 80%, var(--fg) 20%)
    }
    .searchBar:hover {
        box-shadow: 0 6px 24px color-mix(in srgb, var(--accent) 25%, transparent);
        outline: none;
    }
    .searchBar:focus {
        box-shadow: 0 6px 24px color-mix(in srgb, var(--accent) 25%, transparent);
    }
    .logo-launch {
        animation: logo-launch 900ms cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }
    .logo-return {
        animation: logo-return 900ms cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }
    @keyframes logo-launch {
        from {
            transform: translateY(0);
        }
        to {
            transform: translateY(var(--logo-transform-y));
        }
    }
    @keyframes logo-return {
        from {
            transform: translateY(var(--logo-transform-y));
        }
        to {
            transform: translateY(0);
        }
    }
</style>

<script lang="ts">
    import logo from '$lib/assets/favicon.svg'

    const logoTransformY = '-30vh'
    let logoLaunched = false
    function onSearch(input: string) {
        console.log(input)
    }

    function launchLogo() {
        logoLaunched = !logoLaunched
    }
</script>
