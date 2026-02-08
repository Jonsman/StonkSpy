import logging
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account

# For local testing
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, # Auf DEBUG setzen, um wirklich alles zu sehen
    format='%(levelname)s: %(message)s',
    stream=sys.stdout # Wichtig: Cloud Run fängt stdout ab
)
logger = logging.getLogger(__name__)

# Load environment variables
project_id = os.environ.get("PROJECT_ID")
location = os.environ.get("GCP_REGION")
generative_model = os.environ.get("VERTEXAI_MODEL")
#credentials_string = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

'''
# Prompt the model to generate content
def askVertexAI(companyName):
    logger.debug(f"Initializing Vertex AI with project {project_id} and location {location}")
    # Load credentials from environment variable
    #credentials_data = json.loads(credentials_string)
    #credentials = service_account.Credentials.from_service_account_info(credentials_data)

    # Initialize Vertex AI
    vertexai.init(
        project=project_id,
        location=location,
        #credentials=credentials
    )

    # Load the Gemini model
    model = GenerativeModel(generative_model)
    logger.debug(f"Initialized Vertex AI with model {generative_model}")

    prompt = f"""
    You are a finance expert. Use the latest data available. State the date your data is from.
    You should do it in three steps:
    1. Summarize the company's main business, products and services.
    2. Break down the competetive advantages.
    3. Outline the investment risks.
    Analyze the following company in the style mentioned before: {companyName}.
    If you can't find the company or the input seems incorrect return empty properties. Then set companyName to "Business not found".
    Always include a short and consise disclaimer at the end except if the input is incorrect.
    Style the text in raw JSON format without markdown.
    Name the properties of the JSON object as follows:
    - companyName (include stock ticker if available)
    - dateOfData
    - dataSource
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
            return response.text[7:-4] # remove leading/trailing quotes
        else:
            logger.error(f"No response from Vertex AI")
            return None
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return None
'''

def askVertexAI(companyName):
    project_id = os.environ.get("PROJECT_ID")
    location = os.environ.get("GCP_REGION")
    model_name = os.environ.get("VERTEXAI_MODEL")

    if not all([project_id, location, model_name]):
        logger.error(f"FEHLENDE ENV VARS: Project={project_id}, Location={location}, Model={model_name}")
        return None

    try:
        logger.info(f"Initialisiere Vertex AI für: {companyName}")
        vertexai.init(project=project_id, location=location)
        
        model = GenerativeModel(model_name)
        
        prompt = f"""
        You are a finance expert. Use the latest data available. State the date your data is from.
        You should do it in three steps:
        1. Summarize the company's main business, products and services.
        2. Break down the competetive advantages.
        3. Outline the investment risks.
        Analyze the following company in the style mentioned before: {companyName}.
        If you can't find the company or the input seems incorrect return empty properties. Then set companyName to "Business not found".
        Always include a short and consise disclaimer at the end except if the input is incorrect.
        Style the text in raw JSON format without markdown.
        Name the properties of the JSON object as follows:
        - companyName (include stock ticker if available)
        - dateOfData
        - dataSource
        - businessDescription
        - competitiveAdvantages
        - investmentRisks
        - disclaimer
        """
        
        response = model.generate_content(prompt)
        
        if response and response.text:
            raw_text = response.text.strip()
            logger.debug(f"RAW AI answer: {raw_text}")
            
            # Remove markdown code block if present
            clean_json = raw_text.replace("```json", "").replace("```", "").strip()
            return clean_json
        else:
            logger.error("Empty response from Vertex AI")
            return None

    except Exception as e:
        logger.exception(f"Critical error in askVertexAI: {str(e)}")
        return None




# Create a Flask app
app = Flask(__name__)
CORS(app)

@app.route("/api/askVertexAI", methods=["POST", "OPTIONS"])
def ask_vertex_ai():
    if request.method == "OPTIONS":
        return "", 204

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    companyName = request.json.get("companyName")
    if not companyName:
        return jsonify({"error": "Company name is required"}), 400
    
    try:
        logger.debug(f"Received companyName {companyName}")
        result = askVertexAI(companyName)
        logger.debug(f"Received result from askVertexAI: {result}")
        if result is None:
            return jsonify({"error": "No response from AI service"}), 500
        return result, 200
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

# This is for local testing
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(host="0.0.0.0", port=8080)