from product import Product


class Category:
    """Класс категории продуктов на маркетплейсе"""
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name: str, description: str, product: list[Product]) -> object:
        self.name = name
        self.description = description
        self.__product = product

        Category.total_number_of_unique_products += len(product)
        Category.total_number_of_categories += 1

    def middle_price(self) -> int:
        """Подсчитывает средний ценник всех товаров"""
        try:
            count_price = 0
            for item in self.__product:
                count_price += item.price
            avg_price = count_price / len(self.__product)
            return avg_price

        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:
        result = ''
        for product in self.__product:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return result

    @products.setter
    def products(self, product):
        """Сеттер, принимающий на вход объект товара и добавляющий его в список."""
        if product.quantity == 0:
            raise ValueError("Нельзя добавить товар с нулевым количеством!")

        if isinstance(product, Product):
            self.__product.append(product)
        raise TypeError




    def __len__(self) -> int:
        """Магический метод, считающий количество продуктов из общего числа всех продуктов на складе."""
        counter = 0
        for product in self.__product:
            counter += product.quantity
        return counter

    def __str__(self) -> str:
        """Cтроковое отображение в следующем виде: Название категории, количество продуктов: 200 шт."""
        return f'{self.name}, количество продуктов: {len(self)}'


if __name__ == "__main__":
    cat1 = Category("Техника", "Электрические приборы ",
                    [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                             180000.0, 0)])
    cat2 = Category("gjgjjа", "Электрические приборы ",
                    [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                             180000.0, 5)])
    print(cat1)
    len(cat1)
    print(cat1.middle_price())
    #cat2.products = Product('name', 'description', 80000.0, 0)