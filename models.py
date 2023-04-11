from admin import db


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # parent_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return self.name


class Medicines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True,nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),nullable=False)
    categories = db.relationship('Categories')
    country = db.Column(db.String(40),nullable=False)
    active_substance_id = db.Column(db.Integer, db.ForeignKey('active_substances.id'))
    active_substance = db.relationship('Active_substances')
    representative = db.Column(db.String(50))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'))
    manufacturer = db.relationship('Manufacturers')
    code_atx = db.Column(db.String(50))
    price = db.Column(db.Float,nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255), nullable=True, default='default.jpg')



class Manufacturers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)


class Active_substances(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)


class Cart_items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'))
    medicine = db.relationship('Medicines')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    quantity = db.Column(db.Integer)


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    price = db.Column(db.Integer)


class Order_items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'))
    medicine = db.relationship('Medicines')
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship('Orders')
    quantity = db.Column(db.Integer)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True,nullable=False)
    email = db.Column(db.String(64), unique=True,nullable=False)
    phone = db.Column(db.String(64), unique=True,nullable=False)
    password = db.Column(db.String(128))
