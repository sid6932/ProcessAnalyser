from flask import Flask, app, render_template, request

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route("/")
def index():
    return render_template("index.html")





