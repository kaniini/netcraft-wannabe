#!/usr/bin/env python

from flask import Flask, request, jsonify
import requests
import json
import re
app = Flask(__name__)

match_pat = re.compile('^(.+)\.netcraft\.dereferenced\.org$')

@app.route("/", methods=['POST'])
def index():
    global match_pat

    qt = request.form['qtype']
    if qt not in ['TXT', 'ANY']:
        return "[]"

    matches = match_pat.match(request.form['qname'])
    if not matches:
        return "[]"

    dn = matches.group(1)
    if dn[0] == '*':
        return "[]"
    uri = 'http://' + dn
    r = requests.get(uri)

    result = {
        "qname": request.form['qname'],
        "qtype": "TXT",
        "ttl": 300,
        "content": r.headers['Server']
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
