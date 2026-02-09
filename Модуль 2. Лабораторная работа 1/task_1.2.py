import doctest


class Bottle:
    def __init__(self, material: str, volume_ml: int, color: str):
        """
        Создание объекта "Бутылка"

        :param material: Материал бутылки
        :param volume_ml: Объем в мл
        :param color: Цвет бутылки

        """
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Материал не может быть пустым")
        self.material = material.strip()

        if not isinstance(volume_ml, int):
            raise TypeError("Объем должен быть целым числом")
        if volume_ml <= 0:
            raise ValueError("Объем должен быть положительным")
        self.volume_ml = volume_ml

        if not isinstance(color, str) or not color.strip():
            raise ValueError("Цвет не может быть пустым")
        self.color = color.strip()

        self._is_open = False
        self._liquid_ml = 0

    def open_bottle(self) -> bool:
        """
        Открытие бутылки.

        :return: True если бутылка открыта

        """
        if not self._is_open:
            self._is_open = True
            return True
        return False

    def close_bottle(self) -> bool:
        """
        Закрытие бутылки.

        :return: True если бутылка закрыта

        """
        if self._is_open:
            self._is_open = False
            return True
        return False

    def pour_liquid(self, amount_ml: int) -> int:
        """
        Наливание жидкости в бутылку.

        :param amount_ml: Количество жидкости в мл
        :return: Текущее количество жидкости в мл после наливания
        :raise ValueError: Если количество жидкости отрицательное
        :raise RuntimeError: Если бутылка закрыта

        """
        if not self._is_open:
            raise RuntimeError("Откройте бутылку")

        if not isinstance(amount_ml, int):
            raise TypeError("Количество жидкости должно быть целым числом")
        if amount_ml <= 0:
            raise ValueError("Количество жидкости должно быть положительным")

        self._liquid_ml = min(self.volume_ml, self._liquid_ml + amount_ml)
        return self._liquid_ml

    def __str__(self) -> str:
        """
        Возвращает строковое представление бутылки.

        :return: Строковое представление

        """
        status = "открыта" if self._is_open else "закрыта"
        return f"Бутылка {self.volume_ml}мл ({self.material}, {self.color}): жидкость {self._liquid_ml}мл, статус: {status}"


if __name__ == "__main__":
    doctest.testmod()

    # Создание бутылки
    water_bottle = Bottle("пластик", 750, "синий")
    print(f"Создана бутылка: {water_bottle}")

    # Открытие
    if water_bottle.open_bottle():
        print("Бутылка открыта!")
    else:
        print("Не удалось открыть бутылку")

    # Наливание жидкости
    try:
        current_volume = water_bottle.pour_liquid(500)
        print(f"Налили 500мл, теперь в бутылке: {current_volume} мл")
    except RuntimeError as e:
        print(f"Ошибка: {e}")

    # Наливание еще
    try:
        current_volume = water_bottle.pour_liquid(300)
        print(f"Налили 300мл, теперь в бутылке: {current_volume}мл")
    except RuntimeError as e:
        print(f"Ошибка: {e}")

    # Закрытие
    if water_bottle.close_bottle():
        print("Бутылка закрыта!")
