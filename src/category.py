from product import Product


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
    def products(self) -> str:
        result = ''
        for product in self.__product:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return result


    @products.setter
    def products(self, product):
        """Сеттер, принимающий на вход объект товара и добавляющий его в список."""
        self.__product.append(product)



if __name__ == "__main__":
    cat1 = Category("Техника", "Электрические приборы ", [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)])
    #cat1.add_product = "увлажнитель воздуха"
    # print(cat1.name)
    # print(cat1.description)
    # print(cat1.__product)
    #print(cat1.add_product)
    print(cat1.products)
