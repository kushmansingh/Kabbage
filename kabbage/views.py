import requests

from flask import jsonify, request, render_template, make_response

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
    if resp.status_code != 200:
        response = make_response(resp.text)
        response.status_code = resp.status_code
        return response
    return jsonify(resp.json())

@app.route('/result', methods=['GET'])
def result():
    return render_template('result.html', qual=request.args.to_dict())


