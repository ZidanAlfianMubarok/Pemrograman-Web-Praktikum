from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "ZIDAN ALFIAN MUBAROK 5230411107"

if __name__ == "__main__":
    app.run(debug=True)