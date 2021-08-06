from flask import Flask, request, jsonify
import cosmos
import uuid


# init
app = Flask(__name__)
conn = cosmos.connect()
product_container = cosmos.get_container('Products', conn)




# routes
@app.route('/api/products', methods=['GET'])
def get_all():
    result = cosmos.get_all(product_container)
    products = []

    for item in result:
        products.append({ 'id': item['id'], 'name': item['name'], 'description': item['description'], 'category': item['category'] })

    return jsonify(products)





@app.route('/api/products', methods=['POST'])
def post():
    id = str(uuid.uuid4())
    name = request.json['name']
    description = request.json['description']
    category = request.json['category']

    cosmos.insert_one(product_container, { 'id': id, 'name': name, 'description': description, 'category': category, 'partitionKey': 'Product' })
    result = cosmos.get_one(product_container, id, 'Product')

    product = {
        'id': result['id'],
        'name': result['name'],
        'description': result['description'],
        'category': result['category']
    }

    return jsonify(product)


# run
if __name__ == '__main__':
    app.run(debug=True)