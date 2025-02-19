
    class Animal:

        def __init__(self, name: str, age: int) -> None:

            self._name = name  # Непубличный атрибут, чтобы защитить данные о имени
            self._age = age  # Непубличный атрибут, чтобы защитить данные о возрасте

        def __str__(self) -> str:
            """
            Возвращает строковое представление животного.

            :return: Строка с информацией о животном.
            """
            return f"{self._name}, {self._age} years old"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление животного.

            :return: Формальная строка с информацией о животном.
            """
            return f"Animal(name='{self._name}', age={self._age})"

        def speak(self) -> str:
            """
            Издает звук животного.

            :return: Сообщение о звуке животного.
            """
            return "Some sound"

    class Cat(Animal):
            """
            Класс для кошек, наследующий от Animal.
            """

            def __init__(self, name: str, age: int, color: str) -> None:
                """
                Инициализация кошки.

                :param name: Имя кошки.
                :param age: Возраст кошки.
                :param color: Цвет кошки.
                """
                super().__init__(name, age)  # Вызов конструктора базового класса
                self._color = color  # Непубличный атрибут, чтобы защитить данные о цвете

            def __str__(self) -> str:
                """
                Возвращает строковое представление кошки.

                :return: Строка с информацией о кошке.
                """
                return f"{super().__str__()} - Color: {self._color}"

            def speak(self) -> str:
                """
                Издает звук кошки.

                :return: Сообщение о звуке кошки.
                """
                return "Meow!"

