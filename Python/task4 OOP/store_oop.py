# App store program
# first the user logs in then he buys from the store
import random


class Product:
    """this class is for the product that we sell"""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def deduct_stock(self, qty):
        """reduce the stock after buying"""
        self.quantity -= qty

    def __str__(self):
        """print the product info"""
        return f"{self.name} | ${self.price:.2f} | {self.quantity} units"


class Login:
    """this class is for the login interface"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.code = None

    def verify_username(self, username):
        """check if the username is correct"""
        return username == self.username

    def verify_password(self, password):
        """check if the password is correct"""
        return password == self.password

    def generate_code(self):
        """make a random code of 5 numbers"""
        self.code = random.randint(10000, 99999)
        return self.code

    def verify_code(self, code):
        """check if the code is the same as the generated one"""
        return code == self.code

    def login(self, input_fn=input):
        print("--- User Login ---")

        username = input_fn("Enter your username: ").strip()
        if not self.verify_username(username):
            print("Invalid username.")
            return False

        password = input_fn("Enter your password: ").strip()
        if not self.verify_password(password):
            print("Invalid password.")
            return False

        code = self.generate_code()
        print(f"Your verification code is: {code}")

        entered = int(input_fn("Enter the verification code: ").strip())
        if not self.verify_code(entered):
            print("Invalid verification code.")
            return False

        print("Welcome!")
        return True


class Store:
    """this class is for the store that sells the products"""

    def __init__(self, products):
        self.products = products
        self.cart = []
        self.currency_rates = {"USD": 1.0, "EUR": 0.92, "EGP": 48.0}

    def display_catalog(self):
        """print the products in the catalog as a table"""
        print("\n--- Electronics Catalog ---")
        print(f"{'Product':<20}{'Price':<10}In stock")
        print("-" * 42)
        for product in self.products:
            print(f"{product.name:<20}${product.price:<9.2f}{product.quantity}")

    def find_product(self, name):
        """search for a product using its name"""
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def select_product(self, input_fn=input):
        """ask for the product name until the user enters a valid one"""
        while True:
            name = input_fn("Enter the product name: ").strip()
            product = self.find_product(name)
            if product is None:
                print("Product not found. Please enter a valid product name.")
            else:
                return product

    def check_stock(self, product, input_fn=input):
        """ask for the quantity until it works with the stock"""
        while True:
            qty = int(input_fn("Enter the quantity: ").strip())
            if qty <= 0:
                print("Quantity must be positive.")
            elif qty > product.quantity:
                print("Insufficient stock. Please enter a different quantity.")
            else:
                return qty

    def calculate_discount(self, qty, price):
        """5% discount for every 5 units, max 25%"""
        discount_percent = min(25, (qty // 5) * 5)
        discounted_price = price * (1 - discount_percent / 100)
        return discount_percent, discounted_price


    def calculate_total(self):
        """sum all the prices in the cart after the discount"""
        total = 0.0
        for product, qty in self.cart:
            _, discounted_price = self.calculate_discount(qty, product.price)
            total += discounted_price * qty
        return total

    def apply_charge(self, option):
        """delivery is 200 and pick-up is 50"""
        return 200.0 if option.lower() == "delivery" else 50.0

    def convert_currency(self, total, currency):
        """convert the total to the chosen currency, if not valid use USD"""
        currency = currency.upper()
        if currency not in self.currency_rates:
            currency = "USD"
        rate = self.currency_rates[currency]
        return currency, total * rate

    def checkout(self, input_fn=input):
        """run the whole store flow for one order"""
        self.display_catalog()

        keep_shopping = True
        while keep_shopping:
            product = self.select_product(input_fn)
            qty = self.check_stock(product, input_fn)

            discount_percent, discounted_price = self.calculate_discount(qty, product.price)
            print(f"Discount applied: {discount_percent}% "
                  f"(discounted price ${discounted_price:.2f}/unit)")

            self.cart.append((product, qty))

            more = input_fn("Do you want to add more products? (yes/no): ").strip().lower()
            keep_shopping = more == "yes"

        subtotal = self.calculate_total()
        print(f"Subtotal after discounts: ${subtotal:.2f}")

        option = input_fn("Delivery or pick-up? ").strip().lower()
        charge = self.apply_charge(option)
        print(f"{option.capitalize()} charge: ${charge:.2f}")

        total_usd = subtotal + charge

        currency = input_fn("Select currency (USD, EUR, EGP): ").strip()
        currency, total_converted = self.convert_currency(total_usd, currency)
        print(f"Final total: {total_converted:.2f} {currency}")

        # after the order we remove the quantity from the stock
        for product, qty in self.cart:
            product.deduct_stock(qty)

        print("Your order is on its way. Thank you!")


def main():
    """run the app"""
    products = [
        Product("Laptop", 1500.0, 10),
        Product("Phone", 800.0, 20),
        Product("Headphones", 120.0, 50),
        Product("Tablet", 500.0, 15),
    ]

    login = Login("admin", "1234")
    if login.login():
        store = Store(products)
        store.checkout()


if __name__ == "__main__":
    main()