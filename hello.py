from flask import Flask

# creates an instance of the Flask object
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"
if __name__ == '__main__':
    app.run(port=5000, debug=True)
