import doctest


class Door:
    def __init__(self, material: str, width_cm: int, height_cm: int):
        """
        Создание объекта "Дверь"

        :param material: Материал двери
        :param width_cm: Ширина в см
        :param height_cm: Высота в см

        """
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Материал не может быть пустым")
        self.material = material.strip()

        if not isinstance(width_cm, int):
            raise TypeError("Ширина должна быть целым числом")
        if width_cm <= 0:
            raise ValueError("Ширина должна быть положительной")
        self.width_cm = width_cm

        if not isinstance(height_cm, int):
            raise TypeError("Высота должна быть целым числом")
        if height_cm <= 0:
            raise ValueError("Высота должна быть положительной")
        self.height_cm = height_cm

        self._is_open = False
        self._is_locked = False

    def open(self) -> bool:
        """
        Открытие двери.

        :return: True если дверь открыта

        """
        if not self._is_locked and not self._is_open:
            self._is_open = True
            return True
        return False

    def close(self) -> bool:
        """
        Закрытие двери.

        :return: True если дверь закрыта

        """
        if self._is_open:
            self._is_open = False
            return True
        return False

    def lock(self) -> bool:
        """
        Запирание двери.

        :return: True если дверь заперта

        """
        if not self._is_open and not self._is_locked:
            self._is_locked = True
            return True
        return False

    def __str__(self) -> str:
        """
        Возвращает строковое представление двери.

        :return: Строковое представление

        """
        status = "открыта" if self._is_open else "закрыта"
        lock_status = "заперт" if self._is_locked else "отрыт"
        return f"Дверь {self.width_cm}x{self.height_cm} см ({self.material}), статус: {status}, замок: {lock_status}"


if __name__ == "__main__":
    doctest.testmod()

    # Создание двери
    front_door = Door("дуб", 95, 215)
    print(f"Создана дверь: {front_door}")

    # Открытие
    if front_door.open():
        print("Дверь открыта!")
    else:
        print("Не удалось открыть дверь")

    # Закрытие
    if front_door.close():
        print("Дверь закрыта!")

    # Запирание
    if front_door.lock():
        print("Дверь заперта!")

    # Попытка открыть запертую дверь
    if front_door.open():
        print("Дверь открыта!")
    else:
        print("Не удалось открыть запертую дверь")
