from flask import request
from flask_restful import Resource
from models.dish import Dish


class DishesByCategory(Resource):
    def get(self):
        category_id=request.args.get('category_id')
        recipes = Dish.query.filter_by(category_id=category_id).all()
        return [recipe.serialize() for recipe in recipes]
   

