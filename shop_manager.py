import json
from shop import Product


class ShopManage:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_product(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        products = []

        for item in data:
            product = Product(item["name"], item["price"])
            products.append(product)

        return products

    def save_product(self, products):
        data = []

        for product in products:
            data.append({"name": product.name,"price": product.price})

        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def add_product(self, product):
        products = self.load_product()
        products.append(product)
        self.save_product(products)

    def show_all(self):
        return self.load_product()

    def delete_product(self, name):
        products = self.load_product()
        new_products = []

        for product in products:
            if product.name != name:
                new_products.append(product)

        self.save_product(new_products)

    def update(self, old_name, new_product):
        products = self.load_product()

        for product in products:
            if product.name == old_name:
                product.name = new_product.name
                product.price = new_product.price

        self.save_product(products)