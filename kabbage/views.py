from flask import jsonify, request, render_template

from kabbage import app

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'GET':
        return render_template('home.html', error=error)

