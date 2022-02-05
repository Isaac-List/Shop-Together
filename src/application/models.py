from .config import db, mm
  
class Item(db.Model):
    __tablename__ = "items"
    text = db.Column(db.String(200), primary_key=True)
    quantity = db.Column(db.Integer)
    complete = db.Column(db.Boolean)

class ItemSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        sqla_session = db.session
