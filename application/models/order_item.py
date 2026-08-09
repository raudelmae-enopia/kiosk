from database import db
from sqlalchemy import Numeric

class OrderItem(db.Model):
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(
        db.Integer,
        db.ForeignKey("orders.id"),
        nullable=False
    )

    menu_item_size_id = db.Column(
        db.Integer,
        db.ForeignKey("menu_item_sizes.id"),
        nullable=False
    )

    quantity = db.Column(db.Integer, default=1)
    
    unit_price = db.Column(
        Numeric(10, 2),
        nullable=False
    )
    
    notes = db.Column(db.Text)

    order = db.relationship(
        "Order",
        back_populates="order_items"
    )

    menu_item_size = db.relationship(
        "MenuItemSize",
        back_populates="order_items"
    )

    def __repr__(self):
        return f"<OrderItem {self.id}>"
    