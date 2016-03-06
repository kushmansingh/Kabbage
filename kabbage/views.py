import requests

from flask import jsonify, request, render_template

from kabbage import app

BUSINESS_TYPES = [
    'Accounting',
    'Amusement',
    'AutoRepair',
    'BusinessServices',
    'Catering',
    'ChildCare',
    'ComputerServices',
    'ConsumerGoodsRetailStore',
    'ConsumerGoodsOnlineStore',
    'ConsumerGoodsOnlineAndOffline',
    'Construction',
    'Dentists',
    'DryCleaning',
    'Equipment',
    'FoodService',
    'Grocery',
    'Health',
    'HomeRepair',
    'Hotels',
    'Insurance',
    'Janitorial',
    'Landscape',
    'Optometrists',
    'Physicians',
    'Restaurants',
    'Salons',
    'Taxis',
    'Trucking',
    'Veterinarians']

@app.route('/')
def home():
    return render_template('home.html', businessTypes=BUSINESS_TYPES)

@app.route('/prequal')
def prequal():
    href = 'https://api.kabbage.com/v2/prequalify'
    args = request.query_string
    args += '&api_key=' + app.config['API_KEY']
    resp = requests.post(href, data=args)
    return None


