from db import db

class Dish(db.Model):
    __tablename__ = "dish_dish"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    is_gluten_free = db.Column(db.Boolean, default=False)
    is_vegeterian = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category_category.id'),nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "description":self.description,
            "image":self.image,
            "is_gluten_free":self.is_gluten_free,
            "is_vegeterian":self.is_vegeterian,
            "category":self.category.name
        }
