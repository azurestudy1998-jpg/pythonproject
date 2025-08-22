from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python 3.13 on Azure Web App 🚀"

if __name__ == "__main__":
    # Azure uses port from environment variable
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
