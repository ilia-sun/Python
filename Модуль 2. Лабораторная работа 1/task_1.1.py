import doctest


class Window:
    def __init__(self, width_cm: int, height_cm: int, is_double_glazed: bool):
        """
        Создание объекта "Окно"

        :param width_cm: Ширина окна в см
        :param height_cm: Высота окна в см
        :param is_double_glazed: Двойное остекление

        """
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

        if not isinstance(is_double_glazed, bool):
            raise TypeError("Тип остекления должен быть булевым значением")
        self.is_double_glazed = is_double_glazed

        self._is_open = False
        self._is_locked = False

    def open_window(self) -> bool:
        """
        Открытие окна.

        :return: True если окно открыто

        """
        if not self._is_locked and not self._is_open:
            self._is_open = True
            return True
        return False

    def close_window(self) -> bool:
        """
        Закрытие окна.

        :return: True если окно закрыто

        """
        if self._is_open:
            self._is_open = False
            return True
        return False

    def lock_window(self) -> bool:
        """
        Запирание окна.

        :return: True если окно заперто

        """
        if not self._is_open and not self._is_locked:
            self._is_locked = True
            return True
        return False


if __name__ == "__main__":
    doctest.testmod()

    # Создание окна
    room_window = Window(140, 160, True)
    print(f"Создано окно: {room_window.width_cm}x{room_window.height_cm} см")
    print(f"Двойное остекление: {'да' if room_window.is_double_glazed else 'нет'}")
    print(f"Статус: открыто={room_window._is_open}, заперто={room_window._is_locked}")

    # Открытие
    if room_window.open_window():
        print("Окно открыто")
    else:
        print("Не удалось открыть окно")

    # Закрытие
    if room_window.close_window():
        print("Окно закрыто")

    # Запирание
    if room_window.lock_window():
        print("Окно заперто")

    # Попытка открыть запертое окно
    if room_window.open_window():
        print("Окно открыто")
    else:
        print("Не удалось открыть запертое окно")