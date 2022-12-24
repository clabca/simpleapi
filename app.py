from flask import Flask, jsonify, request
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

from products import products
@app.route('/')
def saludo():
    return 'Hola Desde Flask '   # ruta para probar


@app.route('/ping')
def ping():
    return 'pong!!!'   # ruta para probar

@app.route('/ping2')
def ping2():
    return jsonify({"mensaje": "pong!!!"})   # ruta para probar entrega json

@app.route('/products1', methods=['GET', 'POST'])
def getproducts1():
    return jsonify(products)

@app.route('/products', methods=['GET'])
def getproducts():
    return jsonify({"Productos" : products, "Titulo" :"Lista de Productos"})


@app.route('/products1/<string:product_name>')
def getProduct1(product_name):
    print(product_name)
    return  "Recibido"

@app.route('/products2/<string:product_name>')
def getProduct2(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    print(productsFound)
    return  jsonify({"producto" : productsFound[0]})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound)>0):
        return  jsonify({"producto" : productsFound[0]})
    return  jsonify({"Mensaje" : "Producto no encontrado"})


@app.route('/products1', methods=['POST'])
def addProduct1():
    return "Recibido"

@app.route('/products2', methods=['POST'])
def addProduct2():
    print(request.json)
    return "Recibido"

@app.route('/products', methods=['POST'])
def addProduct():
    Newproduct = {
        "name": request.json['name'],
        "price": request.json['price'], 
        "Cantidad": request.json['Cantidad']
    }
    products.append(Newproduct)
    return jsonify({"msje":"Producto Agregado","Productos":products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound)>0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['Cantidad'] = request.json['Cantidad']
        return jsonify({
            "mensaje" : "Producto Actualizado",
            "Producto" : productsFound[0]
        })
    return  jsonify({"Mensaje" : "Producto no encontrado"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def DeleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound)>0):
        products.remove(productsFound[0])
        return jsonify({
            "mensaje" : "Producto eliminado",
            "Productos" : products
        })
    return  jsonify({"Mensaje" : "Producto no encontrado"})



if __name__ == '__main__':
    app.run(debug=True)

