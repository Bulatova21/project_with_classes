class Category:
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product

        Category.total_number_of_unique_products += len(product)
        Category.total_number_of_categories += 1


class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    cat1 = Category("Техника", "Электрические приборы ", ["утюг", "пылесос", "кофемашинка"])
    cat2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    print(cat1.name)
    print(cat1.description)
    print(cat1.product)
    print(cat2.name)
    print(cat2.description)
    print(cat2.price)
    print(cat2.quantity)