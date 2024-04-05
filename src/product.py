
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


if __name__ == "__main__":
    cat2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    dog2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 160000.0, 4)
    # print(cat2.name)
    # print(cat2.description)
    # print(cat2.price)
    # print(cat2.quantity)
    #print(cat2)
    res = cat2 + dog2
    print(res)