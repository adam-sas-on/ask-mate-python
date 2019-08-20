from flask import Flask, render_template, url_for

main = Flask(__name__)

@main.route('/')
def index():
	return "Running on"

if __name__ == '__main__':
	main.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
	)

