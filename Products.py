class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Назва товару: {self.name}")
        print(f"Ціна за одиницю: {self.price}")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {self.calculate_total_price()}")

if __name__ == "__main__":
    product = Product("Айфони", 45799, 5)
    product.display_info()