from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL de la API FAKE
URL = "https://fakestoreapi.com/products"


products = requests.get(URL).json()

#Listar productos
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

def get_element(product_id):
    isFound = False
    for product in products:
        if product["id"] == product_id:
            isFound = True
            return product 
    return None  

#Listar productos por id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_element(product_id)
    print(product)  
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(product)

def max_id():
    maximo = products[0]['id']
    for product in products:
        if product['id'] > maximo:
            maximo = product['id']
    return maximo

#Metodo agregar un nuevo producto
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json() 
    product_id = max_id() + 1  
    data['id'] = product_id  
    products.append(data)  
    return jsonify(data), 201  

#Metodo eliminar un producto
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    products = [p for p in products if p['id'] != product_id]
    return jsonify({"message": "Producto eliminado correctamente"}), 200

#Metodo modificar un producto
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    product.update(data)
    return jsonify(product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
