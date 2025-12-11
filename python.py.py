from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask API!"

@app.route("/hello")
def hello():
    return "Hello Chandu!"

@app.route("/info")
def info():
    return "This is the info API running on Flask."

if __name__ == '__main__':
    app.run(debug=True)
