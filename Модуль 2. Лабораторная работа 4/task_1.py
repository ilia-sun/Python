if __name__ == "__main__":
    class Lamp:
        # Базовый класс лампы.
        # У лампы есть производитель, мощность и состояние (включена или выключена).
        # Атрибут состояния сделан непубличным, чтобы нельзя было напрямую менять состояние лампы без использования методов.

        def __init__(self, brand: str, power: float) -> None:
            # Конструктор класса Lamp
            # brand — производитель лампы
            # power — мощность лампы в ваттах
            self.brand: str = brand
            self.power: float = power
            self._is_on: bool = False

        def __str__(self) -> str:
            # Метод возвращает строку с информацией о лампе
            state = "включена" if self._is_on else "выключена"
            return f"Лампа {self.brand}, мощность {self.power}Вт, состояние: {state}"

        def __repr__(self) -> str:
            # Метод используется для отображения объекта в консоли
            return f"Lamp(brand='{self.brand}', power={self.power}, is_on={self._is_on})"

        def turn_on(self) -> None:
            # Метод включает лампу
            self._is_on = True

        def turn_off(self) -> None:
            # Метод выключает лампу
            self._is_on = False

        def energy_consumption(self, hours: float) -> float:
            # Метод считает сколько энергии потребила лампа
            # hours — время работы в часах
            return self.power * hours


    class LEDLamp(Lamp):
        # Дочерний класс светодиодной лампы.
        # Наследует свойства обычной лампы, но добавляет яркость.

        def __init__(self, brand: str, power: float, brightness: int) -> None:
            # Конструктор расширяет конструктор базового класса
            super().__init__(brand, power)
            self.brightness: int = brightness

        def __str__(self) -> str:
            # Переопределённый метод строкового представления
            state = "включена" if self._is_on else "выключена"
            return f"LED лампа {self.brand}, {self.power}Вт, яркость {self.brightness} lm, состояние: {state}"

        def __repr__(self) -> str:
            # Представление объекта для разработчика
            return f"LEDLamp(brand='{self.brand}', power={self.power}, brightness={self.brightness}, is_on={self._is_on})"

        def energy_consumption(self, hours: float) -> float:
            # Метод перегружен.
            # Причина: светодиодные лампы потребляют меньше энергии,поэтому используется коэффициент эффективности.
            efficiency: float = 0.8
            return (self.power * hours) * efficiency

        def change_brightness(self, new_brightness: int) -> None:
            # Метод для изменения яркости лампы
            self.brightness = new_brightness
    pass
