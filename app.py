from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "随便写点什么吧!"

if __name__ == "__main__":
    app.run()
