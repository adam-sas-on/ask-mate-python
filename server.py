from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', questions=None)


if __name__ == '__main__':
    app.run(port=8000,
            debug=True)
