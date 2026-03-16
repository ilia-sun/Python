# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Book:
    def __init__(self, title: str, page_count: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param page_count: Общее количество страниц в книге

        Примеры:
        >>> book = Book("Война и Мир", 1225)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title
        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.page_count = page_count
    def get_page_count(self) -> int:
        ...
    def get_title_length(self) -> int:
        ...


class Smartphone:
    def __init__(self, brand: str, battery_capacity: int):
        """
        Создание и подгтовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param battery_capacity: Емоксть батареии

        Примеры:
        >>> phone = Smartphone("Apple", 3000)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость батареи должна быть целым числом")
        if battery_capacity <= 0:
            raise ValueError("Емкость батареи должна быть положительным")
        self.battery_capacity = battery_capacity
    def get_brand_uppercase(self) -> str:
        ...
    def check_battery_health(self, cycles_used: int) -> str:
        if not isinstance(cycles_used, int):
            raise TypeError("Количество циклов должно быть целым числом")
        if cycles_used < 0:
            raise ValueError("Количество циклов не может быть отрицательным")
        ...
class Box:
    def __init__(self, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Коробка"

        :param width: Ширина коробки в см
        :param height: Высота коробки в см

        Примеры:
        >>> box = Box(30.0, 20.0)
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина коробки должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина коробки должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота коробки должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота коробки должна быть положительным числом")
        self.height = height
    def calculate_area(self) -> float:
        ...
    def get_dimensions_ratio(self) -> float:
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
