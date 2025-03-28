from flask import Flask, request, jsonify
from llama3_api import summarise_text
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#API route
@app.route("/summarise", methods=["POST"])
def summarise_route():
    data = request.get_json()
    transcript = data.get("transcript")
    
    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400

    summary = summarise_text(transcript)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)

# app = Flask(__name__)

# @app.route("/members")
# def members():  
#     return {"members": ["Member1", "Member2", "Member3"]}

# if __name__ == "__main__":
#       app.run(debug=True)