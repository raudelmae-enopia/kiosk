from sqlalchemy import Numeric
from database import db


class MenuItemSize(db.Model):
    __tablename__ = "menu_item_sizes"

    id = db.Column(db.Integer, primary_key=True)

    menu_item_id = db.Column(
        db.Integer,
        db.ForeignKey("menu_items.id"),
        nullable=False
    )

    size = db.Column(
        db.String(20),
        nullable=False
    )

    price = db.Column(
        Numeric(10, 2),
        nullable=False
    )

    menu_item = db.relationship(
        "MenuItem",
        back_populates="sizes"
    )

    order_items = db.relationship(
        "OrderItem",
        back_populates="menu_item_size"
    )