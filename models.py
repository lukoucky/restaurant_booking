from flask_sqlalchemy import SQLAlchemy

database_name = "restaurant_booking"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    """ setup_db(app)
        binds a flask application and a SQLAlchemy service
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class RestaurantTable(db.Model):
    __tablename__ = 'restaurant_table'

    id = db.Column(db.Integer, primary_key=True)
    number_of_chairs = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False, unique=True)

    def __init__(self, name, number_of_chairs):
        self.name = name
        self.number_of_chairs = number_of_chairs

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<Restaurant Table - id: {self.id}, name: {self.name}, chairs: {self.number_of_chairs}>'
