from main import app
from database import db
from models.category import Category
from models.menu_item import MenuItem
from models.menu_item_size import MenuItemSize


def seed_database():
    with app.app_context():

        # Clear existing menu data
        MenuItemSize.query.delete()
        MenuItem.query.delete()
        Category.query.delete()

        db.session.commit()

        # =========================
        # CATEGORIES
        # =========================

        coffee_matcha = Category(
            name="Artisanal Coffee & Matcha",
            display_order=1,
            active=True
        )

        bakery = Category(
            name="Japanese Bakery & Pastries",
            display_order=2,
            active=True
        )

        snacks = Category(
            name="Light Dishes & Snacks",
            display_order=3,
            active=True
        )

        db.session.add_all([
            coffee_matcha,
            bakery,
            snacks
        ])

        db.session.commit()

        # =========================
        # MENU ITEMS
        # =========================

        tokyo_drip = MenuItem(
            category_id=coffee_matcha.id,
            name="Tokyo-Style Drip Coffee",
            image="placeholder.jpg",
            available=True,
            display_order=1
        )

        espresso = MenuItem(
            category_id=coffee_matcha.id,
            name="Espresso",
            image="placeholder.jpg",
            available=True,
            display_order=2
        )

        americano = MenuItem(
            category_id=coffee_matcha.id,
            name="Americano",
            image="placeholder.jpg",
            available=True,
            display_order=3
        )

        cafe_latte = MenuItem(
            category_id=coffee_matcha.id,
            name="Café Latte",
            image="placeholder.jpg",
            available=True,
            display_order=4
        )

        cappuccino = MenuItem(
            category_id=coffee_matcha.id,
            name="Cappuccino",
            image="placeholder.jpg",
            available=True,
            display_order=5
        )

        matcha_latte = MenuItem(
            category_id=coffee_matcha.id,
            name="Premium Uji Matcha Latte",
            image="placeholder.jpg",
            available=True,
            display_order=6
        )

        butter_croissant = MenuItem(
            category_id=bakery.id,
            name="Butter Croissant",
            image="placeholder.jpg",
            available=True,
            display_order=1
        )

        matcha_muffin = MenuItem(
            category_id=bakery.id,
            name="Matcha-Infused Muffin",
            image="placeholder.jpg",
            available=True,
            display_order=2
        )

        strawberry_shortcake = MenuItem(
            category_id=bakery.id,
            name="Strawberry Shortcake",
            image="placeholder.jpg",
            available=True,
            display_order=3
        )

        handmade_anpan = MenuItem(
            category_id=bakery.id,
            name="Handmade Anpan",
            image="placeholder.jpg",
            available=True,
            display_order=4
        )

        tamagosando = MenuItem(
            category_id=snacks.id,
            name="Tamagosando",
            image="placeholder.jpg",
            available=True,
            display_order=1
        )

        mini_katsu_sliders = MenuItem(
            category_id=snacks.id,
            name="Mini Katsu Sliders",
            image="placeholder.jpg",
            available=True,
            display_order=2
        )

        smoked_salmon_toast = MenuItem(
            category_id=snacks.id,
            name="Smoked Salmon Toast",
            image="placeholder.jpg",
            available=True,
            display_order=3
        )

        db.session.add_all([
            tokyo_drip,
            espresso,
            americano,
            cafe_latte,
            cappuccino,
            matcha_latte,
            butter_croissant,
            matcha_muffin,
            strawberry_shortcake,
            handmade_anpan,
            tamagosando,
            mini_katsu_sliders,
            smoked_salmon_toast
        ])

        db.session.commit()

        # =========================
        # COFFEE & MATCHA SIZES
        # =========================

        db.session.add_all([

            # Tokyo-Style Drip Coffee
            MenuItemSize(
                menu_item_id=tokyo_drip.id,
                size="S",
                price=170
            ),
            MenuItemSize(
                menu_item_id=tokyo_drip.id,
                size="M",
                price=200
            ),
            MenuItemSize(
                menu_item_id=tokyo_drip.id,
                size="L",
                price=230
            ),

            # Espresso
            MenuItemSize(
                menu_item_id=espresso.id,
                size="S",
                price=180
            ),
            MenuItemSize(
                menu_item_id=espresso.id,
                size="M",
                price=210
            ),
            MenuItemSize(
                menu_item_id=espresso.id,
                size="L",
                price=240
            ),

            # Americano
            MenuItemSize(
                menu_item_id=americano.id,
                size="S",
                price=190
            ),
            MenuItemSize(
                menu_item_id=americano.id,
                size="M",
                price=220
            ),
            MenuItemSize(
                menu_item_id=americano.id,
                size="L",
                price=250
            ),

            # Café Latte
            MenuItemSize(
                menu_item_id=cafe_latte.id,
                size="S",
                price=220
            ),
            MenuItemSize(
                menu_item_id=cafe_latte.id,
                size="M",
                price=250
            ),
            MenuItemSize(
                menu_item_id=cafe_latte.id,
                size="L",
                price=280
            ),

            # Cappuccino
            MenuItemSize(
                menu_item_id=cappuccino.id,
                size="S",
                price=230
            ),
            MenuItemSize(
                menu_item_id=cappuccino.id,
                size="M",
                price=260
            ),
            MenuItemSize(
                menu_item_id=cappuccino.id,
                size="L",
                price=290
            ),

            # Premium Uji Matcha Latte
            MenuItemSize(
                menu_item_id=matcha_latte.id,
                size="S",
                price=260
            ),
            MenuItemSize(
                menu_item_id=matcha_latte.id,
                size="M",
                price=290
            ),
            MenuItemSize(
                menu_item_id=matcha_latte.id,
                size="L",
                price=320
            ),

            # =========================
            # BAKERY & PASTRIES
            # =========================

            MenuItemSize(
                menu_item_id=butter_croissant.id,
                size="Regular",
                price=140
            ),

            MenuItemSize(
                menu_item_id=matcha_muffin.id,
                size="Regular",
                price=160
            ),

            MenuItemSize(
                menu_item_id=strawberry_shortcake.id,
                size="Regular",
                price=240
            ),

            MenuItemSize(
                menu_item_id=handmade_anpan.id,
                size="Regular",
                price=150
            ),

            # =========================
            # LIGHT DISHES & SNACKS
            # =========================

            MenuItemSize(
                menu_item_id=tamagosando.id,
                size="Regular",
                price=190
            ),

            MenuItemSize(
                menu_item_id=mini_katsu_sliders.id,
                size="Regular",
                price=260
            ),

            MenuItemSize(
                menu_item_id=smoked_salmon_toast.id,
                size="Regular",
                price=280
            )
        ])

        db.session.commit()

        print("Database seeded successfully!")
        print("13 menu items added.")


if __name__ == "__main__":
    seed_database()