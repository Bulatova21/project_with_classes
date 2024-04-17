from abc import ABC, abstractmethod


class ProductAbstract(ABC):
    """Абстрактный класс для продукта"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
