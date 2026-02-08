import doctest


class Plant:
    def __init__(self, min_amount_water: float, amount_water: float):
        """
        Создание и подготовка к работе объекта "Растение"

        :param min_amount_water: Минимальное кол-во воды для растания (мл)
        :param amount_water: Кол-во воды в данный момент (мл)

        Примеры:
        >>> plant = Plant(200, 10)
        """
        if not isinstance(min_amount_water, (int, float)):
            raise TypeError('Мин. кол-во воды должно быть типа int или float')
        if min_amount_water <= 0:
            raise ValueError('Мин. кол-во воды должно быть положительным числом')
        self.min_amount_water = min_amount_water

        if not isinstance(amount_water, (int, float)):
            raise TypeError('Кол-во воды должно быть типа int или float')
        if amount_water < 0:
            raise ValueError('Кол-во воды не может быть отрицательным числом')
        self.amount_water = amount_water

    def grow(self) -> bool:
        """
        Функция, которая проверяет достаточно ли воды для роста растения

        :return: Достаточно ли воды для роста растения

        Примеры:
        >>> plant = Plant(200, 10)
        >>> plant.grow()
        """
        ...

    def add_water(self, water: float) -> None:
        """
        Функция, которая добавляет кол-во воды на 'water'

        :param water: Кол-во воды, которое добавляем растению

        Примеры:
        >>> plant = Plant(200, 10)
        >>> plant.add_water(220)
        """

        if not isinstance(water, (int, float)):
            raise TypeError('Добавляемый рост должен быть типа int или float')
        if water < 0:
            raise ValueError('Добавляемый рост должен быть положительным числом')

        ...


class Hero:
    def __int__(self, hp: float, heal: float, attack: float):
        """
        Создание и подготовка к работе объекта "Герой"

        :param hp: Максимальное кол-во здоровья у героя
        :param heal: Кол-во здоровья, которое герой может восстановить за ход
        :param attack: Кол-во урона, который наносит герой за ход

        Примеры:
        >>> hero = Hero(200, 10, 5.5)
        """

        if not isinstance(hp, (int, float)):
            raise TypeError("Кол-во здоровья должно быть типа int или float")
        if hp <= 0:
            raise ValueError("Кол-во здоровья должен быть положительным")
        self.hp = hp

        if not isinstance(heal, (int, float)):
            raise TypeError("Кол-во получаемого здоровья должно быть типа int или float")
        if heal < 0:
            raise ValueError("Кол-во получаемого здоровья не должен быть отрицательным")
        self.heal = heal
        
        if not isinstance(attack, (int, float)):
            raise TypeError("Кол-во урона должно быть типа int или float")
        if attack <= 0:
            raise ValueError("Кол-во урона должен быть положительным")
        self.attack = attack

    def heal_hero(self) -> float:
        """
        Функция, которая восполяет здоровье на определённое число заданное изначально и возвращает кол-во здоровья
        после применения функции

        :return: Кол-во здоровья после применения функции

        :raise ValueError: Если здоровье у героя уже максимальное, то вызываем ошибку

        Примеры:
        >>> hero = Hero(200, 10, 5)
        >>> hero.heal_hero()
        """

        ...

    def get_status(self) -> float:
        """
        Функция, которая возвращает показатели героя

        :return: Возвращает показатели героя

        Примеры:
        >>> hero = Hero(190, 10, 5)
        >>> hero.get_status()
        """

        ...

    def get_attack(self, attack: float) -> float:
        """
        Функция получения урона от врага
        :param attack: Кол-во получаемого урона

        :return: Возвращаем кол-во здоровья после получения урона
        """
        if isinstance(attack, (int, float)):
            raise TypeError('Кол-во получаемого урона должен тип int или float')
        if attack <= 0:
            raise ValueError('Кол-во получаемого урона должен быть положительным')

        ...


# TODO Написать 3 класса с документацией и аннотацией типов

class Door:
    def __init__(self, key: bool, lock: bool):
        """
        Создание и подготовка к работе объекта "Дверь"
        :param key: Имеется ли ключ от двери (bool)
        :param lock: Заперта ли дверь (bool)

        Пример:
        >>> door = Door(True, False)
        """

        if type(key) is not bool:
            raise TypeError('Имеется ли ключ должен типа bool')
        if type(lock) is not bool:
            raise TypeError('Заперта ли дверь должен типа bool')

    def lock_unlock(self) -> None:
        """
        Функция, которая изменияет параметр 'lock' на противоположную при наличии ключа

        :raise ValueError: Если нету ключа, то выводим ошибку

        Примеры:
        >>> door = Door(True, False)
        >>> door.lock_unlock()
        """

        ...

    def get_key(self) -> None:
        """
        Функция, которая меняет параметр 'key' на 'True'

        :raise ValueError: Если параметр 'key' уже имеет значение 'True', то выводим ошибку

        Примеры:
        >>> door = Door(False, True)
        >>> door.get_key()
        """

        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
