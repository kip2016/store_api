from flask import jsonify, make_response, request
from flask_restful import Api, Resource

cart = []


class Products(Resource):
    # Get all cart entries
    def get(self):
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Success",
            'My orders': cart
        }), 200)

    # Add to cart
    def post(self):

        id = len(cart) + 1
        data = request.get_json()
        name = data['name']
        description = data['description']
        price = data['price']

        item = {
            'id': id,
            'name': name,
            'description': description,
            'price': price
        }

        cart.append(item)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Post Success",
            'My Cart': cart
        }), 201)


class SingleProduct(Resource):
    # Get a single cart entry
    def get(self, orderID):
        order = [order for order in cart if order['id'] == orderID]
        if len(order) == 1:
            return make_response(jsonify({
                                 'Status': 'Ok',
                                 'Message': "Success",
                                 'My order': order
                                 }), 200)

class SaleOrder(Resource):
    # Get all sales orders
    def get(self):
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Success",
            'My sales': cart
        }), 200)

    #add a sale order
    def post(self):

        id = len(cart) + 1
        data = request.get_json()
        name = data['name']
        description = data['description']
        price = data['price']

        item = {
            'id': id,
            'name': name,
            'description': description,
            'price': price
        }

        cart.append(item)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Post Success",
            'My Cart': cart
        }), 201)


class SingleSale(Resource):
    # Get a single sale order
    def get(self, orderID):
        order = [order for order in cart if order['id'] == orderID]
        if len(order) == 1:
            return make_response(jsonify({
                                 'Status': 'Ok',
                                 'Message': "Success",
                                 'My order': order
                                 }), 200)
    

class UserLogin(Resource):
        def post(self):
            data = request.get_json()
            if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
                return "You are logged in."
            return make_response('could not verify!',401,{
                'www-Authenticate': 'Basic realm= "Login required"'
            })
