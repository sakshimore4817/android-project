v# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/sandesh')
def hello():
    name = request.args.get("name", "sandesh")
    return f'Hello, {escape(name)}!'
