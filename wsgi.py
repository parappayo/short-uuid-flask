from flask import Flask
import json
import short_uuid


app = Flask(__name__)


@app.route("/")
def main():
    return json.dumps({
        'uuids': [short_uuid.generate() for _ in range(10)]
    })
