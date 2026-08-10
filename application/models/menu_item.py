from database import db


class MenuItem(db.Model):
    __tablename__ = "menu_items"

    id = db.Column(db.Integer, primary_key=True)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    available = db.Column(db.Boolean, default=True)
    display_order = db.Column(db.Integer, default=0)

    category = db.relationship(
        "Category",
        back_populates="menu_items"
    )
    
    # normalized structure// cleaner

    # order_items = db.relationship(
    #     "OrderItem",
    #     back_populates="menu_item"
    # )
    
    sizes = db.relationship(
        "MenuItemSize",
        back_populates="menu_item",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<MenuItem {self.name}>"