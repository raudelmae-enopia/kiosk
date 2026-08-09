from flask import Flask, render_template
from flask_socketio import SocketIO

from config import Config
from database import db

from models import Category, MenuItem, Order, OrderItem

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading"
)

@app.route("/")
def index():
    return render_template("kiosk.html")

@app.route("/barista")
def barista():
    return render_template("barista.html")

def register_routes():
    """
    Register application routes.

    Route modules will be imported here during the refactor.
    """
    pass



if __name__ == "__main__":
    register_routes()

    socketio.run(
        app,
        host="0.0.0.0",
        port=5961,
        debug=True
    )
    
with app.app_context():
    db.create_all()