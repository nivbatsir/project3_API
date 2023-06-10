from db import db

class Category(db.Model):
    __tablename__ = "category_category"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    dishes = db.relationship('Dish', backref='category')

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "recipes":[dish.serialize() for dish in self.dishes]
        }

