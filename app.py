from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to ProfKay Cloud Portfolio</h1>
    <p>Project 04 - Google Cloud Run</p>
    <p>This application is running on Cloud Run.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
