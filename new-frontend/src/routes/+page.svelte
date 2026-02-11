<script>
    import {SearchPage, CompanyInformation} from '$lib';

    let showCompanyInformation = false;

    function handleSearch() {
        showCompanyInformation = !showCompanyInformation;
    }
</script>

<div class="searchPage">
    <div class="searchStack">
        <div>
            <SearchPage onSearched={handleSearch} />
        </div>
        <div class="companySection" class:visible={showCompanyInformation}>
            <CompanyInformation/>
        </div>
    </div>
</div>

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
    .searchStack {
        width: 100%;
        display: grid;
        justify-items: center;
        gap: 16px;
        animation: content-return 900ms cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }
    .companySection {
        width: 100%;
        opacity: 0;
        transform: translateY(24px);
        max-height: 0;
        overflow: hidden;
    }
    .companySection.visible {
        animation: company-show 700ms cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }
    @keyframes content-launch {
        from {
            transform: translateY(0);
        }
        to {
            transform: translateY(-8vh);
        }
    }
    @keyframes content-return {
        from {
            transform: translateY(-8vh);
        }
        to {
            transform: translateY(0);
        }
    }
    @keyframes company-show {
        from {
            opacity: 0;
            transform: translateY(24px);
            max-height: 0;
        }
        to {
            opacity: 1;
            transform: translateY(0);
            max-height: 95vh;
        }
    }
</style>
