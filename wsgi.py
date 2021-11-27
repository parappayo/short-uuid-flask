from flask import Flask
import short_uuid


app = Flask(__name__)


@app.route("/")
def main():
    result = short_uuid.generate()
    return f'{{"uuid":"{result}"}}'
