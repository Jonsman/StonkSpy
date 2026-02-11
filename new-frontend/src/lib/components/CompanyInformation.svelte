<section class="main grid grid-cols-2 gap-4 rounded-2xl">
    <div class="boxed">
        <CornerLabel text="Facts" side="left" />
        <img src={logo} style="display: block; margin-inline: auto;" alt="">
        <div>
            <ul class="proConList">
                <li>
                    <strong>Business Units:</strong>
                    <ul>
                    {#each report.company_report.business_units as item}
                        <li>
                            {item}
                        </li>
                    {/each}
                    </ul>
                </li>
                {#each getKeyFinancialDataString(report.company_report.key_financial_data) as item}
                    <li>
                        <strong>{item.split(':')[0]}:</strong>
                        {item.split(':')[1]}
                    </li>
                {/each}
            </ul>
        </div>
    </div>
    <div class="boxed centerSection">
        <CornerLabel text="Description" side="right" />
        <div>
            {#each report.company_report.company_overview.description.split(". ") as line}
                {line.endsWith(".") ? line : line+"."}
                <br/>
            {/each}
        </div>
    </div>
    <div class="boxed" style="--box-color: var(--pro);">
        <CornerLabel text="Pro" side="left" color="var(--pro)" />
        <ul class="proConList">
            {#each report.company_report.advantages as item}
                <li>
                    <strong>{item.description}</strong>
                    <ul>
                        {#each item.facts as fact}
                            <li>{fact}</li>
                        {/each}
                    </ul>
                </li>
            {/each}
        </ul>
    </div>
    <div class="boxed" style="--box-color: var(--con); --box-brightness: 40%;">
        <CornerLabel text="Con" side="right" color="var(--con)" />
        <ul class="proConList">
            {#each report.company_report.disadvantages as item}
                <li>
                    <strong>{item.description}</strong>
                    <ul>
                        {#each item.facts as fact}
                            <li>{fact}</li>
                        {/each}
                    </ul>
                </li>
            {/each}
        </ul>
    </div>
</section>

<style>
    .main {
        padding: 16px;
        min-width: 90%;
        grid-auto-rows: 1fr;
    }
    .centerSection {
        justify-items: center;
    }
    .boxed {
        --box-color: var(--accent);
        --box-brightness: 25%;
        background-color: color-mix(in srgb, var(--bg) 90%, var(--text) 10%);
        border: 2px solid color-mix(in srgb, var(--box-color) 40%, transparent);
        border-radius: 16px;
        padding: 2.75rem 0.75rem 0.75rem;
        position: relative;
        height: 100%;
    }
    .boxed:hover {
        box-shadow: 0 6px 24px color-mix(in srgb, var(--box-color) var(--box-brightness), transparent);
    }
    .proConList {
        list-style: disc;
        padding-left: 1.25rem;
    }
    .proConList ul {
        list-style: circle;
        padding-left: 1.25rem;
        margin-top: 0.25rem;
    }
</style>

<script lang="ts">
    import CornerLabel from '$lib/components/CornerLabel.svelte';
    import logo from '$lib/assets/favicon.svg'
    import { rawCompanyReport } from '$lib/data/companyReportExample';

    type CompanyReport = {
        company_report: {
            company_overview: { description: string };
            business_units: string[];
            key_financial_data: {
                annual_revenue: number;
                net_income: number;
                gross_profit_margin: number;
                operating_expenses: number;
                market_capitalization: number;
                debt_to_equity_ratio: number;
                pe_ratio: number;
            };
            advantages: Array<{ description: string; facts: string[] }>;
            disadvantages: Array<{ description: string; facts: string[] }>;
            top_competitors: Array<{
                name: string;
                description: string;
                size: string;
                key_markets: string[];
                pe_ratio: number;
            }>;
        };
    };

    function isCompanyReport(value: unknown): value is CompanyReport {
        const v = value as CompanyReport;
        return !!v?.company_report?.company_overview?.description;
    }

    function mapToCompanyReport(json: unknown): CompanyReport {
        if (!isCompanyReport(json)) {
            throw new Error('Invalid CompanyReport JSON');
        }
        return json;
    }
    
    function getKeyFinancialDataString(
        data: CompanyReport['company_report']['key_financial_data']
    ): string[] {
        const usd = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
        const num = new Intl.NumberFormat('en-US', { maximumFractionDigits: 2 });

        const fmtMoney = (v: number | null | undefined) =>
            v == null ? 'N/A' : usd.format(v);
        const fmtNum = (v: number | null | undefined) =>
            v == null ? 'N/A' : num.format(v);
        const fmtPct = (v: number | null | undefined) =>
            v == null ? 'N/A' : `${num.format(v)}%`;

        return [
            `Annual Revenue: ${fmtMoney(data.annual_revenue)}`,
            `Net Income: ${fmtMoney(data.net_income)}`,
            `Gross Profit Margin: ${fmtPct(data.gross_profit_margin)}`,
            `Operating Expenses: ${fmtMoney(data.operating_expenses)}`,
            `Market Cap: ${fmtMoney(data.market_capitalization)}`,
            `Debt/Equity: ${fmtNum(data.debt_to_equity_ratio)}`,
            `P/E Ratio: ${fmtNum(data.pe_ratio)}`
        ];
    }

    const parsed = JSON.parse(rawCompanyReport);
    const report = mapToCompanyReport(parsed);
</script>
