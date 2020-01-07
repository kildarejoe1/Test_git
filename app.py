from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "This is home page!!!"


@app.route("/hello/<username>")
def hello(username):
    return 'Why Hello %s!\n' % username


if __name__ == "__main__":
    app.run(host="0.0.0.0")
