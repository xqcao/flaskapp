from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def hello():
    data = {
        "title": "flask App",
        "msg": "-this app try to running on docker"
    }
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
