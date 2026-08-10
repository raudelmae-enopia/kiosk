from flask import Blueprint, redirect, url_for, session, request

from models import MenuItemSize

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")


@cart_bp.route("/add", methods=["POST"])
def add_to_cart():
    size_id = request.form.get("menu_item_size_id", type=int)

    if not size_id:
        return redirect(url_for("home.index"))

    size = MenuItemSize.query.get_or_404(size_id)

    cart = session.get("cart", {})

    key = str(size.id)

    if key in cart:
        cart[key]["quantity"] += 1
    else:
        cart[key] = {
            "quantity": 1
        }

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("index"))