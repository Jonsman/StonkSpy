import os
from dotenv import load_dotenv, find_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel
import markdown

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Get variables from .env file
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")

# Initialize Vertex AI
vertexai.init(
    project=project_id,
    location=location
)

# Load the Gemini model
model = GenerativeModel("gemini-1.5-flash-002")

company = input("What company do you want to analyze: ")
print(f"Analyzing the financials of {company}...")

prompt = f"""
You are a finance expert. State the date your data is from.
You should do it in three steps:
1. Summarize the company's main business, products and services.
2. Break down the competetive advantages.
3. Outline the investment risks.
Analyze the following company in the style mentioned before: {company}.
Always include a disclaimer at the end.
Style the text in markdown format.
"""

try:
    response = model.generate_content(prompt)
    with open("output.md", "w") as f:
        f.write(markdown.markdown(response.text))
except Exception as e:
    print(f"Error: {e}")