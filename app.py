from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase 
from product import product

db = dbase.dbConnection()

app = Flask(__name__)

#rutas de la aplicacion
@app.route('/')
def home():
    product = db ['products']
    productsReceived = product.find()
    return render_template('agregar.py', product = productsReceived)

#agregar
@app.route('', methods=['POST'])
def addProduct():
    products = request.form['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        product = product(name, price, quantity)
        products.insertOne(product.toDBCollection())
        response = jsonify({
            'name': name,
            'price': price,
            'quantity': quantity
        })
        return redirect(url_for('home'))
    else:
        return notFound()
    
#eliminar
@app.route('/delete/<string:product_name>')
def delete(product_name):
    product = db ['products']
    product.delete_one({'name': product_name})
    return redirect(url_for('home'))

#editar
@app.route('', methods=['POST'])
def edit(product_name):
    products = db ['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one({'name': product_name}, {'$set':{'name': name, 'price': price, 'quantity': quantity}})
        Response = jsonify({'message': 'Producto' + product_name + 'Actualizado Correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound
    
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado' + request.url,
        'status': '404 Not Found'
    }
    Response= jsonify(message)
    Response.status_code = 404
    return Response 
if __name__ == '__main__':
    app.run(debug=True, port=4000)