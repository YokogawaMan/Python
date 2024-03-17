class Calculator:
    """
        Класс, представляющий калькулятор для комплексных чисел.

        Attributes:
            logger (Logger): Экземпляр класса Logger для ведения журнала операций.
    """

    def __init__(self, logger):
        """
            Инициализирует объект Calculator.

            Parameters:
                logger (Logger): Экземпляр класса Logger для ведения журнала операций.
        """
        self.logger = logger

    def add(self, number_1, number_2):
        """
            Выполняет сложение двух комплексных чисел.

            Parameters:
                number_1 (ComplexNumber): Первое комплексное число.
                number_2 (ComplexNumber): Второе комплексное число.

            Returns:
                ComplexNumber: Результат операции сложения.
        """
        result = number_1.add(number_2)
        self.logger.log(f"Adding {number_1} and {number_2} = {result}")
        return result

    def subtract(self, number_1, number_2):
        """
            Выполняет вычитание двух комплексных чисел.

            Parameters:
                number_1 (ComplexNumber): Первое комплексное число.
                number_2 (ComplexNumber): Второе комплексное число.

            Returns:
                ComplexNumber: Результат операции вычитания.
        """
        result = number_1.subtract(number_2)
        self.logger.log(f"Subtracting {number_1} and {number_2} = {result}")
        return result

    def multiply(self, number_1, number_2):
        """
            Выполняет умножение двух комплексных чисел.

            Parameters:
                number_1 (ComplexNumber): Первое комплексное число.
                number_2 (ComplexNumber): Второе комплексное число.

            Returns:
                ComplexNumber: Результат операции умножения.
        """
        result = number_1.multiply(number_2)
        self.logger.log(f"Multiplying {number_1} and {number_2} = {result}")
        return result

    def divide(self, number_1, number_2):
        """
            Выполняет деление двух комплексных чисел.

            Parameters:
                number_1 (ComplexNumber): Первое комплексное число.
                number_2 (ComplexNumber): Второе комплексное число.

            Returns:
                ComplexNumber: Результат операции деления.
        """
        result = number_1.divide(number_2)
        self.logger.log(f"Dividing {number_1} and {number_2} = {result}")
        return result
