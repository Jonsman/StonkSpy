<section class="mainSection">
    <div class="logo" hidden="true">LOGO PLACEHOLDER 🦍</div>
    <img class="logo" src={logo} alt="StonkSpy is nice"/>
    <div>
        <input class="searchBar rounded-2xl"
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
</style>

<script lang="ts">
    import logo from '$lib/assets/favicon.svg'
    function onSearch(input:string) {
        console.log(input)
    }
</script>