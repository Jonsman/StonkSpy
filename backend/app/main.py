import logging
from llm import askVertexAI  # Ensure this import exists
from flask import Flask, request, jsonify
from flask_cors import CORS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a Flask app
app = Flask(__name__)
CORS(app, resources={
    r"/askVertexAI": {
        "origins": "*",
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route("/")
def index():
    return "Running!"

@app.route("/askVertexAI", methods=["POST"])
def ask_vertex_ai():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    companyName = request.json.get("companyName")
    if not companyName:
        return jsonify({"error": "Company name is required"}), 400
    
    try:
        result = askVertexAI(companyName)
        if result is None:
            return jsonify({"error": "No response from AI service"}), 500
        return result, 200
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=5000, debug=True)