import unittest, requests, json, sys
from sm_api import test, returnAll, returnOne, createProd, salesAll, salesOne, createSale

class Test_flask_api(unittest.TestCase):
    def setup(self):
        pass

    def test_test(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.json(), {'message': 'It works'})

    def test_returnAll(self):
        response = requests.get('http://localhost:5000/api/v1/all_products')
        self.assertEqual(response.json(), {'products': 
                                                    [{'name': 'Rice'}, 
                                                    {'name': 'Maize'}, 
                                                    {'name': 'Coffee'}, 
                                                    {'name': 'Sugar'}, 
                                                    {'name': 'Barley'}]
                                                })

    def test_returnOne(self):
        response = requests.get('http://localhost:5000/api/v1/Sugar')
        self.assertEqual(response.json(), {'product': {'name': 'Sugar'}})
    
    #def test_createProd(self):
     #   response = requests.post('http://localhost:5000/api/v1/all_products',{'name':'Yams'})
     #   self.assertIn(response.text,{'name':'Yams'})
        

    def test_salesAll(self):
        '''Ensures all sales returns a size of 5''' 
        response = requests.get('http://localhost:5000/api/v1/sales')
        #print(response.json())
        self.assertEqual(len(response.json()['sales']),5)

    def test_salesOne(self):
        response = requests.get('http://localhost:5000/api/v1/sales/C003')
        self.assertEqual(response.json(), {"result": {
                                                "price": 2800, 
                                                "product_id": "C003", 
                                                "product_name": "Coffee", 
                                                "units_sold": 100
                                            }
                                            })
    
 #   def test_createSale(self):
 #       response = requests.get('http://localhost:5000/api/v1/sales')
 #       self.assertEqual(response.json(), {}) #Need help here

if __name__ == '__main__':
    unittest.main()