import logging
from llm import askVertexAI
from flask import Flask, request, jsonify, send_from_directory

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create a Flask app
app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/askVertexAI", methods=["POST", "OPTIONS"])
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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    #app.run(host="0.0.0.0", port=5000, debug=True)