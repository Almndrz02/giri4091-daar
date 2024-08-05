from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

URL = "https://fakestoreapi.com/products"

@app.route('/products', methods=['GET'])
def get_products():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Esto lanzará una excepción si la solicitud fue insatisfactoria
        products = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_id(product_id):
    try:
        response = requests.get(f"{URL}/{product_id}")
        response.raise_for_status()
        product = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(product)

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    try:
        response = requests.post(URL, json=new_product)
        response.raise_for_status()
        added_product = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(added_product), 201

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        response = requests.delete(f"{URL}/{product_id}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Producto eliminado correctamente"}), 200

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.json
    try:
        response = requests.put(f"{URL}/{product_id}", json=updated_product)
        response.raise_for_status()
        product = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(product)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)