import os
import json
from dotenv import load_dotenv, find_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel
import logging
from google.oauth2 import service_account

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Get variables from .env file
#project_id = os.getenv("PROJECT_ID")
#location = os.getenv("LOCATION")
#generative_model = os.getenv("GENERATIVE_MODEL")

project_id = os.environ.get("PROJECT_ID")
location = os.environ.get("LOCATION")
generative_model = os.environ.get("GENERATIVE_MODEL")
credentials_string = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

# Initialize logging
logger = logging.getLogger(__name__)

def askVertexAI(companyName):
    logger.debug(f"Initializing Vertex AI with project {project_id} and location {location}")
    # Load credentials from string
    credentials_data = json.loads(credentials_string)
    credentials = service_account.Credentials.from_service_account_info(credentials_data)

    # Initialize Vertex AI
    vertexai.init(
        project=project_id,
        location=location,
        credentials=credentials
    )

    # Load the Gemini model
    model = GenerativeModel(generative_model)
    logger.debug(f"Initialized Vertex AI with model {generative_model}")

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
    logger.debug(f"Generated prompt: {prompt}")

    try:
        response = model.generate_content(prompt)
        logger.debug(f"Received response from Vertex AI: {response}")
        if response and response.text:
            return response.text[7:-4]
        else:
            logger.error(f"No response from Vertex AI")
            return None
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return None