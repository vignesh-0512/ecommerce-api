from flask import request, jsonify
from app import app
from app.models import get_all_products, get_product_by_id, create_product

@app.route('/api/products', methods=['GET'])
def products():
    return get_all_products()

@app.route('/api/products/<int:product_id>', methods=['GET'])
def product(product_id):
    return get_product_by_id(product_id)

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    return create_product(name, description, price)
