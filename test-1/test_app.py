from app import app, request
from unittest import TestCase



class CurrencyConvertTestCase(TestCase):
    def test_convert_form(self):
        with app.test_client() as client:

            res = client.get('/convert-form')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('From Currency', html)


    def test_convert_form_submit(self):
        with app.test_client() as client:

            

            resp = client.post('/convert-form-submit', data = {'fromcurrency' : 'USD', 'tocurrency' : 'GBP', 'totalamount' : '50'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('USD', html)
            self.assertIn('GBP', html)
            self.assertIn('50', html)            

    
    
