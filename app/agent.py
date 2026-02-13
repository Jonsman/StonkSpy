from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.apps.app import App
from pydantic import BaseModel, Field
from typing import List, Optional

from .config import config


class CompanyOverview(BaseModel):
    description: str = Field(description="A summary of the company's business.")

class KeyFinancialData(BaseModel):
    annual_revenue: Optional[float] = Field(None, description="Total annual revenue.")
    net_income: Optional[float] = None
    gross_profit_margin: Optional[float] = None
    operating_expenses: Optional[float] = None
    market_capitalization: Optional[float] = None
    debt_to_equity_ratio: Optional[float] = None
    pe_ratio: Optional[float] = None

class AnalysisPoint(BaseModel):
    description: str
    facts: List[str]

class Competitor(BaseModel):
    name: str
    description: str
    size: str
    key_markets: List[str]
    pe_ratio: Optional[float] = None

class CompanyReport(BaseModel):
    company_overview: CompanyOverview
    business_units: List[str]
    key_financial_data: KeyFinancialData
    advantages: List[AnalysisPoint]
    disadvantages: List[AnalysisPoint]
    top_competitors: List[Competitor]

class ReportWrapper(BaseModel):
    company_report: CompanyReport


# Agent Definitions
company_finder = LlmAgent(
    model = config.fast_model,
    name="company_finder",
    description="Finds the company information based on the company name.",
    instruction="""
    You are a research agent.
    Your task is to find a company by its name and provide its stock ticker.
    Utilize Google Search to find reliable information regarding the company and its associated stock ticker.
    When performing a Google Search, prioritize search queries that combine the company name with terms like 'stock ticker', 'stock symbol', or 'NASDAQ'/'NYSE' to quickly identify the relevant information.
    Provide only the company name and its stock ticker.
    Do not include any additional information or context in your response. The output should be concise and limited to the company name and its stock ticker.
    """,
    tools=[google_search],
    output_key="company_name_and_ticker",
)

company_researcher = LlmAgent(
    model = config.worker_model,
    name="company_researcher",
    description="Researches the company information based on the company name.",
    instruction="""
    You are a diligent company researcher tasked with providing a comprehensive report on a given company.
    The company in question is: {company_name_and_ticker}

    Access the most current financial data and news for the company, making use of Google Search. Prioritize official company websites, SEC filings (or equivalent regulatory filings for non-US companies), and reputable financial news sources to ensure information is up-to-date. Your report must be clearly structured with the following headings for each section and should adhere to the specified content and formatting requirements:

    **Company Overview:**
    Briefly describe the company.

    **Business Units:**
    Detail the company's main business units.

    **Key Financial Data:**
    Present the latest available important financial data in a bullet point list. Focus on the following metrics:
    - Annual Revenue
    - Net Income
    - Gross Profit Margin
    - Operating Expenses
    - Market Capitalization
    - Debt-to-Equity Ratio
    - P/E Ratio

    **Advantages:**
    Outline the company's key competitive advantages, supported by 3-5 specific facts.

    **Disadvantages:**
    Describe the company's primary challenges or disadvantages, supported by 3-5 specific facts.

    **Top Competitors:**
    Identify and briefly describe its top 3-5 competitors. For each competitor, compare them based on their size, key markets, and P/E ratio.

    Ensure your analysis is data-driven and concise.
    """,
    tools=[google_search],
    output_key="company_report_written",
    #include_contents="none",
)

company_summarizer = LlmAgent(
    model = config.fast_model,
    name="company_summarizer",
    description="Summarizes the company information based on the company name.",
    instruction="""
    You are an expert data extractor.
    Your task is to extract the relevant information from the provided text and output it as a JSON object.
    Adhere strictly to the specified JSON schema and ensure all fields are correctly populated.

    The input text is as follows:
    {company_report_written}

    **Constraints:**
    - If a value is not present in the text, use `null`. Do not invent data.
    - For "number" fields, provide only the numeric value (e.g., 5000000 instead of "$5M").
    - Ensure the output is a single, valid JSON object.
    - This output must not contain any styling, formatting, or additional commentary.
    """,
    output_schema=ReportWrapper,
    output_key="company_report_structured",
)

research_pipeline_agent = SequentialAgent(
    name="research_pipeline",
    description="A pipeline agent to find a company, research and summarize financial information about it.",
    sub_agents=[
        company_finder,
        company_researcher,
        company_summarizer,
    ]
)

root_agent = research_pipeline_agent
app = App(root_agent=root_agent, name="app")
