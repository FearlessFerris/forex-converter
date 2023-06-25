from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from currency import converted_total

import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
debug = DebugToolbarExtension(app)






@app.route('/home')
def currency_homepage():
    """ Routes to the homepage of my currency converter app """

    return render_template('base.html')






@app.route('/convert-form')
def convert_form():
    """ Routes to form to convert currency """
    
    
    return render_template('convert-form.html')





@app.route('/convert-form-submit', methods = ['POST'])
def convert_form_submit():
    """ Routes the submitted criteria """

    fromcurrency = request.form['fromcurrency']
    tocurrency = request.form['tocurrency']
    totalamount = request.form['totalamount']

    url = f'https://api.exchangerate.host/convert?from={fromcurrency}&to={tocurrency}'
    response = requests.get(url)
    data = response.json()

    date= data['date']
    rate = data['info']['rate']
    convertedtotal = round(float(rate) * float(totalamount), 2)

    if len(fromcurrency) != 3 or len(tocurrency) != 3:
        flash('Your currency code needs to be 3 characters in length!')
        return redirect('/convert-form')
    

    
    return render_template('convert-form-submit.html', convertedtotal = convertedtotal, fromcurrency = fromcurrency, tocurrency = tocurrency, totalamount = totalamount, date = date)


