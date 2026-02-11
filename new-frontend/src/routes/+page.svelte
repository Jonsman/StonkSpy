<script>
    import {SearchPage, CompanyInformation} from '$lib';
</script>

<style>
    .searchPage {
        width: 100%;
        min-height: 100vh;        /* full viewport height */
        box-sizing: border-box;   /* include padding in width/height */
        padding: 10vh 10vw;         /* top/bottom, left/right */
        place-items: center;
        place-content: center;
        overflow: auto;           /* scroll instead of spilling out */
    }
</style>

<div class="searchPage">
    <div style="margin-bottom: 16px;">
        <SearchPage/>
    </div>
    <div hidden={true}>
        <CompanyInformation/>
    </div>
</div>
