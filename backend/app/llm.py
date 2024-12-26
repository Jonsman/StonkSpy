import os
from dotenv import load_dotenv, find_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Get variables from .env file
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")

def askVertexAI(companyName):
    # Initialize Vertex AI
    vertexai.init(
        project=project_id,
        location=location
    )

    # Load the Gemini model
    model = GenerativeModel("gemini-1.5-flash-002")

    #company = input("What company do you want to analyze: ")
    print(f"Analyzing the financials of {companyName}...")

    prompt = f"""
    You are a finance expert. State the date your data is from.
    You should do it in three steps:
    1. Summarize the company's main business, products and services.
    2. Break down the competetive advantages.
    3. Outline the investment risks.
    Analyze the following company in the style mentioned before: {companyName}.
    If you can't find the company or the input seems incorrect return empty properties. Then set companyName to "Business not found".
    Always include a disclaimer at the end except if the input is incorrect.
    Style the text in raw JSON format without markdown.
    Name the properties of the JSON object as follows:
    - companyName (include stock ticker if available)
    - dateOfData
    - businessDescription
    - competitiveAdvantages
    - investmentRisks
    - disclaimer
    """
    try:
        response = model.generate_content(prompt)
        #print(response.text[7:-4])
        return response.text[7:-4]
    except Exception as e:
        return str(e)