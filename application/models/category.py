from database import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    display_order = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)

    menu_items = db.relationship(
        "MenuItem",
        back_populates="category",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Category {self.name}>"