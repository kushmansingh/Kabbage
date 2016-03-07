import requests

from flask import jsonify, request, render_template

from kabbage.forms import BUSINESS_TYPES, PrequalForm
from kabbage import app

@app.route('/')
def home():
    return render_template('home.html',
        businessTypes=[b[0] for b in BUSINESS_TYPES])

@app.route('/prequal', methods=['POST'])
def prequal():
    href = 'https://api.kabbage.com/v2/prequalify'
    form = PrequalForm(request.form)
    if not form.validate():
        errors = form.errors
        response = jsonify(errors)
        response.status_code = 400
        return response
    args = request.form.to_dict()
    args['api_key'] = app.config['API_KEY']
    resp = requests.post(href, data=args)
    return jsonify(resp.json())


