from class_product import Product


class Category:
    """Класс категории продуктов на маркетплейсе"""
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name: str, description: str, product: list[Product]):
        self.name = name
        self.description = description
        self.__product = product

        Category.total_number_of_unique_products += len(product)
        Category.total_number_of_categories += 1

    @property
    def get_product(self):
        """Геттер, возвращающий список product"""
        return self.__product

    @get_product.setter
    def get_product(self, input_product):
        """Сеттер, принимающий на вход объект товара и добавляющий его в список."""
        self.__product += input_product.split("  , ")


    @property
    def list_output(self):
        """Геттер, который будет выводить список товаров в формате:Продукт, 80 руб. Остаток: 15 шт."""
        list_product = []
        for product in self.__product:
            list_product.append(f'{product.name}, {product.price}. Остаток: {product.quantity} шт.')
        return list_product


if __name__ == "__main__":
    cat1 = Category("Техника", "Электрические приборы ", [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)])
    #cat1.add_product = "увлажнитель воздуха"
    # print(cat1.name)
    # print(cat1.description)
    # print(cat1.__product)
    #print(cat1.add_product)
    print(cat1.list_output)
