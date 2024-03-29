
class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity



    @classmethod
    def add_in_list(cls, dict_product: dict):
        """Возвращает объект класса Product из словаря"""
        return cls(dict_product["name"], dict_product["description"], dict_product["price"], dict_product["quantity"])


    @property
    def atr_price(self):
        return self.__price


    @atr_price.setter
    def atr_price(self):
        if self.__price <= 0:
            print("Введена некорректная цена")


if __name__ == "__main__":
    cat2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    print(cat2.name)
    print(cat2.description)
    print(cat2.price)
    print(cat2.quantity)