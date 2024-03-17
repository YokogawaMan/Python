from Logger import Logger
from Calculator import Calculator
from UserInterface import UserInterface
from Title import Title


class Main:
    """
        Главный класс, представляющий точку входа в программу.

        Methods:
            __init__(): Инициализирует объект Main и создает экземпляры логгера, калькулятора и пользовательского интерфейса.
    """

    def __init__(self):
        """
            Инициализирует объект Main и создает экземпляры логгера, калькулятора и пользовательского интерфейса.
        """
        Title()  # Отображает заголовок программы
        self.logger = Logger("calculator_log.txt")  # Инициализирует логгер с именем файла журнала
        self.calculator = Calculator(self.logger)  # Инициализирует калькулятор с экземпляром логгера
        self.user_interface = UserInterface(self.calculator)  # Инициализирует пользовательский интерфейс с экземпляром калькулятора


if __name__ == "__main__":
    main = Main()  # Создает экземпляр класса Main
    main.user_interface.run()  # Запускает пользовательский интерфейс
