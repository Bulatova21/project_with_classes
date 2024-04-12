class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Cтроковое отображение в следующем виде: Название продукта, 80 руб. Остаток: 15 шт."""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Метод складывающий объекты между собой"""
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def add_product(cls, dict_product: dict):
        """Возвращает объект класса Product из словаря"""
        return cls(dict_product["name"], dict_product["description"], dict_product["price"], dict_product["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self):
        if self.__price <= 0:
            print("Введена некорректная цена")


class Smartphone(Product):
    """Класс Смартфон"""

    def __init__(self, name, description, price, quantity, productivity: float, model: str,
                 built_in_memory_capacity: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.productivity = productivity
        self.model = model
        self.built_in_memory_capacity = built_in_memory_capacity
        self.color = color

    def __str__(self) -> str:
        """Cтроковое отображение в следующем виде: Название продукта, 80 руб. Остаток: 15 шт.
         Производительность, модель, объем встроенной памяти, цвет"""
        return (f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт. {self.productivity}, '
                f'{self.model}, {self.built_in_memory_capacity}, {self.color}')

    def __add__(self, other):
        """Метод складывающий объекты между собой"""
        if isinstance(other, Smartphone):
            return self.price * self.quantity + other.__price * other.quantity

        raise TypeError


class LawnGrass(Product):
    """Класс Трава газонная"""
    def __init__(self, name, description, price, quantity, country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Cтроковое отображение в следующем виде: Название продукта, 80 руб. Остаток: 15 шт.
         Страна-производитель, срок прорастания, цвет. """
        return (f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт. {self.country}, '
                f'{self.germination_period} дней, {self.color}')

    def __add__(self, other):
        """Метод складывающий объекты между собой"""
        if isinstance(other, LawnGrass):
            return self.price * self.quantity + other.__price * other.quantity

        raise TypeError

if __name__ == "__main__":
    cat2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    dog2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 160000.0, 4)
    # print(cat2.name)
    # print(cat2.description)
    # print(cat2.price)
    # print(cat2.quantity)
    print(cat2)
    # res = cat2 + dog2
    # print(res)
    smart1 = Smartphone("Samsung Galaxy C22 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 44.69,
                      "Galaxy C23 Ultra",
                      "1Т", "yellow")
    lawn1 = LawnGrass("Samsung Galaxy C22 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "Russia", 14, "зеленый" )
    print(smart1)
    print(lawn1)