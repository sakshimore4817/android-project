v# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/sakshi')
def hello():
    name = request.args.get("name", "sakshi")
    return f'Hello, {escape(name)}!'
