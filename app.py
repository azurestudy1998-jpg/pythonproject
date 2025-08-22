from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS (allows any origin)
CORS(app)

@app.route("/")
def home():
    return "Hello from Python 3.13 on Azure Web App 🚀 (CORS enabled)"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)  # allow external access

