from flask import Flask, render_template
from flask_socketio import SocketIO

from config import Config
from database import db

from models import Category, MenuItem, MenuItemSize, Order, OrderItem
from routes.cart import cart_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading"
)

app.register_blueprint(cart_bp)

# Previous / route

# @app.route("/")
# def index():
#     from services.menu_service import get_categories
#     categories = get_categories()
#     return render_template(
#         "kiosk.html",
#         categories=categories
#     )

@app.route("/")
def index():
    from services.menu_service import get_categories, get_menu_items

    categories = get_categories()
    menu_items = get_menu_items()

    return render_template(
        "kiosk.html",
        categories=categories,
        menu_items=menu_items
    )

@app.route("/barista")
def barista():
    return render_template("barista.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    socketio.run(
        app,
        host="0.0.0.0",
        port=5961,
        debug=True
    )