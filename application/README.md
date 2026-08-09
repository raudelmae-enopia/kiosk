# ☕ Saika Cafe Self-Ordering Kiosk

A self-ordering kiosk system built with **Python**, **Flask**, and **SQLite**.

This project allows customers to browse the café menu, customize their orders, view the total price, and receive a queue number through a tablet interface. Staff can manage incoming orders using a separate dashboard with real-time queue updates.

---

## Features

### Customer Kiosk

- Browse menu by category
- Select beverage sizes
- Add items to cart
- View running total
- Confirm orders
- Receive a queue number
- Live queue display

### Staff Dashboard

- View incoming orders
- Update order status
- Manage the customer queue
- Real-time updates using Socket.IO

---

## Built With

- Python 3.12+
- Flask
- Flask-SQLAlchemy
- Flask-SocketIO
- SQLite
- HTML
- CSS
- JavaScript

---

## Project Structure

```text
application/
│
├── models/
├── routes/
├── services/
├── static/
├── templates/
│
├── main.py
├── database.py
├── config.py
└── seed.py
```

---

## Database

The system uses a normalized SQLite database.

```
Category
    │
    └── MenuItem
            │
            └── MenuItemSize

Order
    │
    └── OrderItem
```

---

## Current Menu

### Coffee & Matcha

- Tokyo Style Drip Coffee
- Espresso
- Americano
- Café Latte
- Cappuccino
- Premium Uji Matcha Latte

### Bakery

- Butter Croissant
- Matcha-Infused Muffin
- Strawberry Shortcake
- Handmade Anpan

### Snacks

- Tamagosando
- Mini Katsu Sliders
- Smoked Salmon Toast

---

## Installation

Clone the repository.

```bash
git clone https://github.com/your-username/saika-cafe-kiosk.git
```

Go to the project folder.

```bash
cd saika-cafe-kiosk/application
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Create the database.

```bash
python database.py
```

Run the application.

```bash
python main.py
```

Open your browser.

```
http://localhost:5961
```

---

## Screenshots

Screenshots will be added as development continues.

---

## License

This project is for educational purposes.

---

## Author

**Raudel Mae Enopia**
DEVTCON BTBI1
Project • 2026
