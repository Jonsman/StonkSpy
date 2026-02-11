<section class="main grid grid-cols-2 gap-4 rounded-2xl">
    <div class="boxed">
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
        <div>
            DESCRIPTION:
            <br/>
            {#each report.company_report.company_overview.description.split(". ") as line}
                {line.endsWith(".") ? line : line+"."}
                <br/>
            {/each}
        </div>
    </div>
    <div class="boxed proBox">
        PRO 📈:
        <br/>
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
    <div class="boxed conBox">
        CON 📉:
        <br/>
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
    :root {
        --pro: #289d32;
        --con: #7a2222;
    }
    .main {
        padding: 16px;
        min-width: 90%;
        grid-auto-rows: 1fr;
    }
    .centerSection {
        justify-items: center;
    }
    .boxed {
        background-color: color-mix(in srgb, var(--bg) 90%, var(--text) 10%);
        border: 2px solid color-mix(in srgb, var(--accent) 40%, transparent);
        box-shadow: 0 6px 24px color-mix(in srgb, var(--accent) 10%, transparent);
        border-radius: 16px;
        padding: 8px;
        height: 100%;
    }
    .boxed.proBox {
        border: 2px solid color-mix(in srgb, var(--pro) 40%, transparent);
    }
    .boxed.proBox:hover {
        box-shadow: 0 6px 24px color-mix(in srgb, var(--pro) 50%, transparent);
    }
    .boxed.conBox {
        border: 2px solid color-mix(in srgb, var(--con) 40%, transparent);
    }
    .boxed.conBox:hover {
        box-shadow: 0 6px 24px color-mix(in srgb, var(--con) 65%, transparent);
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
    import logo from '$lib/assets/favicon.svg'

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

    // Example usage
    const raw = `
    {
        "company_report": {
            "company_overview": {
                "description": "McDonald's Corporation (MCD) is a global leader in the fast-food industry, operating as an American multinational fast-food chain. Founded in 1940 by brothers Richard and Maurice McDonald, it evolved under Ray Kroc who bought the company in 1961. It is now one of the largest and most recognizable restaurant chains globally, known for its quick-service hamburgers, fries, and breakfast items. As of 2023, McDonald's operated over 41,800 restaurants in nearly 120 countries, serving approximately 68 million customers daily. Its headquarters are in Chicago, Illinois."
            },
            "business_units": [
                "U.S. Market",
                "International Operated Markets (IOM)",
                "International Developmental Licensed (IDL) Markets & Corporate"
            ],
            "key_financial_data": {
                "annual_revenue": 26265000000,
                "net_income": 8416000000,
                "gross_profit_margin": null,
                "operating_expenses": 14160000000,
                "market_capitalization": 232140000000,
                "debt_to_equity_ratio": -19.09,
                "pe_ratio": 27.34
            },
            "advantages": [
                {
                    "description": "Strong Brand Recognition and Global Presence",
                    "facts": [
                        "The Golden Arches are recognized worldwide",
                        "Fostering significant customer loyalty across over 100 countries and 43,000 locations"
                    ]
                },
                {
                    "description": "Cost Leadership and Economies of Scale",
                    "facts": [
                        "Employs a cost leadership strategy through bulk purchasing, standardized processes, and efficient operations",
                        "Helps minimize costs and allows for competitive pricing"
                    ]
                },
                {
                    "description": "Franchise Model and Real Estate Holdings",
                    "facts": [
                        "Extensive franchise system (around 95% of restaurants are franchised) provides a scalable business model",
                        "Company's ownership of significant real estate generates stable income beyond food sales"
                    ]
                },
                {
                    "description": "Operational Efficiency and Consistency",
                    "facts": [
                        "Known for its highly detailed systems and processes",
                        "Ensuring speed, consistent quality, and a uniform customer experience globally"
                    ]
                },
                {
                    "description": "Adaptability and Innovation",
                    "facts": [
                        "Adapts its menu to local tastes and preferences while maintaining a core product range",
                        "Embraced digital transformation, including mobile ordering, loyalty programs, and delivery partnerships"
                    ]
                }
            ],
            "disadvantages": [
                {
                    "description": "Changing Consumer Preferences",
                    "facts": [
                        "Increasing demand for healthier and more sustainable dining options",
                        "Challenges traditional fast-food offerings and requires menu adaptation"
                    ]
                },
                {
                    "description": "Intense Competition and Market Saturation",
                    "facts": [
                        "Fast-food industry is highly competitive, with many players also adopting cost leadership strategies",
                        "Leading to market saturation in some areas"
                    ]
                },
                {
                    "description": "Economic Instability and Cost Pressures",
                    "facts": [
                        "Fluctuating consumer spending due to economic instability",
                        "Rising labor costs (e.g., increased minimum wages) and supply chain disruptions can impact profitability and operational costs"
                    ]
                },
                {
                    "description": "Brand Reputation and Health Concerns",
                    "facts": [
                        "Occasionally faces brand reputation issues and criticisms related to the nutritional value of its food and its environmental impact",
                        "Sustainability pressures"
                    ]
                },
                {
                    "description": "Dependency on Delivery Services",
                    "facts": [
                        "Increased reliance on delivery services can lead to new operational complexities",
                        "Potential impact on profit margins"
                    ]
                }
            ],
            "top_competitors": [
                {
                    "name": "Starbucks (SBUX)",
                    "description": "Starbucks is a large multinational coffeehouse chain, one of the most recognized brands globally.",
                    "size": "As of early 2026, its market capitalization is typically in the range of $100 billion to $120 billion.",
                    "key_markets": [
                        "Global, with a strong presence in North America, Asia (especially China), and Europe."
                    ],
                    "pe_ratio": null
                },
                {
                    "name": "Yum! Brands (YUM)",
                    "description": "Yum! Brands is a large fast-food corporation that owns KFC, Pizza Hut, Taco Bell, and The Habit Burger Grill.",
                    "size": "Its market capitalization is typically in the range of $30 billion to $40 billion.",
                    "key_markets": [
                        "Global, with a diverse portfolio targeting various segments (chicken, pizza, Mexican-inspired food). Strong international presence across its brands."
                    ],
                    "pe_ratio": null
                },
                {
                    "name": "Restaurant Brands International (RBI)",
                    "description": "RBI owns Burger King, Tim Hortons, Popeyes Louisiana Kitchen, and Firehouse Subs.",
                    "size": "Its market capitalization is typically in the range of $20 billion to $30 billion.",
                    "key_markets": [
                        "Global, with Burger King being a direct competitor to McDonald's in the burger segment. Tim Hortons dominates the Canadian coffee and donut market, while Popeyes focuses on fried chicken."
                    ],
                    "pe_ratio": null
                },
                {
                    "name": "Wendy's Company (WEN)",
                    "description": "Wendy's is a prominent fast-food chain, primarily focused on burgers.",
                    "size": "Its market capitalization is typically in the range of $4 billion to $6 billion, making it smaller than McDonald's but a significant direct competitor.",
                    "key_markets": [
                        "Primarily North America, with some international presence. Known for its made-to-order burgers and square patties."
                    ],
                    "pe_ratio": null
                }
            ]
        }
    }
    `;
    const parsed = JSON.parse(raw);
    const report = mapToCompanyReport(parsed);
</script>
