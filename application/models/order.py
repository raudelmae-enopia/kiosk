from enum import Enum
from datetime import datetime
from database import db
from sqlalchemy import Numeric


class OrderStatus(Enum):
    PENDING = "Pending"
    PREPARING = "Preparing"
    READY = "Ready"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    queue_number = db.Column(db.Integer, nullable=False, unique=True)

    status = db.Column(
        db.String(20),
        default="Pending",
        nullable=False
    )

    total = db.Column(
    Numeric(10, 2),
    default=0.00,
    nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    order_items = db.relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Order #{self.queue_number}>"