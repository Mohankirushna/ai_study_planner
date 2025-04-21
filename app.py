'''
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend/public")
CORS(app)
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend/public")
CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'dashboard.html')

@app.route('/api/gemini/chat', methods=['POST'])
def chat_with_gemini():
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    print(f"Received message: {user_message}") 
    API_KEY = "AIzaSyDwgRf9-URg-m51UNMIWFgL78KENwPBodY"  # Your actual API key
    model_name = "gemini-2.0-flash-001"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }

    try:
        print(f"Sending request to Gemini with message: {user_message}")
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            gemini_response = response.json()
            if "candidates" in gemini_response:
                message = gemini_response['candidates'][0]['content']['parts'][0]['text']
                print(f"Gemini Response Message: {message}")
                return jsonify({"response": message})
            else:
                return jsonify({"error": "No candidates in response."}), 500
        else:
            return jsonify({"error": response.text}), response.status_code
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({"error": "An error occurred while processing the request."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)
'''
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# Create Flask app
app = Flask(__name__, static_folder="../frontend/public", static_url_path='/')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Serve the main HTML page
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'dashboard.html')

# Serve other static files (CSS, JS, images)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Gemini API chat endpoint
@app.route('/api/gemini/chat', methods=['POST'])
def chat_with_gemini():
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    print(f"[Received]: {user_message}") 

    # Use environment variables to store sensitive information
    API_KEY = os.getenv("AIzaSyDwgRf9-URg-m51UNMIWFgL78KENwPBodY")  # Replace with environment variable for security
    if not API_KEY:
        return jsonify({"error": "API key is missing."}), 500

    model_name = "gemini-2.0-flash-001"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            gemini_response = response.json()
            if "candidates" in gemini_response:
                message = gemini_response['candidates'][0]['content']['parts'][0]['text']
                print(f"[Gemini]: {message}")
                return jsonify({"response": message})
            else:
                return jsonify({"error": "No candidates returned."}), 500
        else:
            print(f"[Error Response]: {response.text}")
            return jsonify({"error": response.text}), response.status_code
    except Exception as e:
        print(f"[Exception]: {str(e)}")
        return jsonify({"error": "An error occurred while processing the request."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)
