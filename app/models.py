from app import mysql
from flask import jsonify

def get_all_products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    return jsonify(products)

def get_product_by_id(product_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    return jsonify(product) if product else ("Product not found", 404)

def create_product(name, description, price):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO products(name, description, price) VALUES (%s, %s, %s)", (name, description, price))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Product created successfully'}), 201
