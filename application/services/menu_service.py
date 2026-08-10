# from models.category import Category
# from models.menu_item import MenuItem


# def get_categories():
#     return (
#         Category.query
#         .filter_by(active=True)
#         .order_by(Category.display_order)
#         .all()
#     )


# def get_menu_items():
#     return (
#         MenuItem.query
#         .filter_by(available=True)
#         .order_by(
#             MenuItem.category_id,
#             MenuItem.display_order
#         )
#         .all()
#     )


from models.category import Category
from models.menu_item import MenuItem


def get_categories():
    return (
        Category.query
        .filter_by(active=True)
        .order_by(Category.display_order)
        .all()
    )


def get_menu_items():
    return (
        MenuItem.query
        .filter_by(available=True)
        .order_by(
            MenuItem.category_id,
            MenuItem.display_order
        )
        .all()
    )