from application import db

class Store(db.Document):
    neighborhood = db.StringField(db_field="n")
    address = db.StringField(db_field="a")
    city = db.StringField(db_field="c")
    state = db.StringField(db_field="st")
    zip = db.StringField(db_field="z")
    phone = db.StringField(db_field="p")
