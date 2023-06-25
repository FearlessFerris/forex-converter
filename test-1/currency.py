from flask import Flask, request
import requests

def converted_total(rate, totalamount):
    """ Calculates the converted Currency """

    fromcurrency = request.form.get('fromcurrency')
    tocurrency = request.form.get('tocurrency')
    totalamount = request.form.get('totalamount')


    url = f'https://api.exchangerate.host/convert?from={fromcurrency}&to={tocurrency}'
    response = requests.get(url)
    data = response.json()

    date= data['date']
    rate = data['info']['rate']
    convertedtotal = round(float(rate) * float(totalamount), 2)



    
    # convertedtotal = round(float(rate) * float(totalamount), 2)