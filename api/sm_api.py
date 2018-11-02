from flask import Flask, jsonify, request
app = Flask(__name__) #define app using flask

#Products List
products = [{'name': 'Rice'}, {'name': 'Maize'}, {'name': 'Coffee'}, {'name': 'Sugar'}, {'name': 'Barley'}]

#Sales Data List
sales = [
        {'product_id': 'R001', 'product_name': 'Rice', 'price': 1500, 'units_sold': 20},
        {'product_id': 'M002', 'product_name': 'Maize', 'price': 1200, 'units_sold': 55},
        {'product_id': 'C003', 'product_name': 'Coffee', 'price': 2800, 'units_sold': 100},
        {'product_id': 'S004', 'product_name': 'Sugar', 'price': 4600, 'units_sold': 250},
        {'product_id': 'B005', 'product_name': 'Barley', 'price': 12500, 'units_sold': 65}
    ]

#tester
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works'})

#Get product catalog
@app.route('/api/v1/all_products', methods=['GET'])
def returnAll():
    return jsonify({'products' : products})

#Get single product input by user/tester
@app.route('/api/v1/<string:product_name>', methods=['GET'])
def returnOne(product_name):
    product = [product for product in products if product['name']==product_name]
    return jsonify({'product': product[0]})

#add a Product
@app.route('/api/v1/all_products', methods=['POST'])
def createProd():
    product = {'name': request.json['name']}
    products.append(product)
    return jsonify({'products' : products})

#Get all sales
@app.route('/api/v1/sales', methods=['GET'])
def salesAll():
    return jsonify({'sales': sales})

#Get single sale input by user/tester
@app.route('/api/v1/sales/<string:prod_id>', methods=['GET'])
def salesOne(prod_id):
    sale = [sale for sale in sales if sale['product_id']==prod_id]
    return jsonify({'result': sale[0]})

#add a sale
@app.route('/api/v1/sales', methods=['POST'])
def createSale():
    sale = {
        'product_id': request.json['product_id'], 
        'product_name': request.json['product_name'], 
        'price': request.json['price'], 
        'units_sold': request.json['units_sold']
        }
   
    sales.append(sale)
    return jsonify({'sales': sales})

#Execute the app in debug mode on localhost with default port=5000
if __name__ == '__main__':
    app.run(debug=True)
