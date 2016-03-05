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

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'GET':
        return render_template('home.html', error=error, businessTypes=BUSINESS_TYPES)

