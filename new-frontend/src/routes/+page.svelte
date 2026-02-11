<script>
    import {SearchPage, CompanyInformation} from '$lib';
</script>

<style>
    .searchPage {
        height: 100vh;
        width: 100vw;
        padding: 5vw 5vh 5vw 5vh;
        place-items: center;
        place-content: center;
    }
</style>

<div class="searchPage">
    <div style="margin-bottom: 16px;">
        <SearchPage/>
    </div>
    <CompanyInformation/>
</div>
