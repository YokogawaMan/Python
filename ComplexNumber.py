class ComplexNumber:
    """
        Класс ComplexNumber представляет комплексное число.

        Attributes:
            real (float): Вещественная часть комплексного числа.
            imaginary (float): Мнимая часть комплексного числа.
    """

    def __init__(self, real, imaginary):
        """
            Конструктор класса ComplexNumber.

            Parameters:
                real (float): Вещественная часть комплексного числа.
                imaginary (float): Мнимая часть комплексного числа.
        """
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        """
            Метод для представления комплексного числа в виде строки.

            Returns:
                str: Строковое представление комплексного числа.
        """
        return f"{self.real} + {self.imaginary}i"

    def add(self, other):
        """
            Метод для сложения двух комплексных чисел.

            Parameters:
                other (ComplexNumber): Другое комплексное число.

            Returns:
                ComplexNumber: Результат сложения комплексных чисел.
        """
        result_real = self.real + other.real
        result_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(result_real, result_imaginary)

    def subtract(self, other):
        """
            Метод для вычитания одного комплексного числа из другого.

            Parameters:
                other (ComplexNumber): Другое комплексное число.

            Returns:
                ComplexNumber: Результат вычитания комплексных чисел.
        """
        result_real = self.real - other.real
        result_imaginary = self.imaginary - other.imaginary
        return ComplexNumber(result_real, result_imaginary)

    def multiply(self, other):
        """
            Метод для умножения двух комплексных чисел.

            Parameters:
                other (ComplexNumber): Другое комплексное число.

            Returns:
                ComplexNumber: Результат умножения комплексных чисел.
        """
        result_real = self.real * other.real - self.imaginary * other.imaginary
        result_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(result_real, result_imaginary)

    def divide(self, other):
        """
            Метод для деления одного комплексного числа на другое.

            Parameters:
                other (ComplexNumber): Другое комплексное число.

            Returns:
                ComplexNumber: Результат деления комплексных чисел.
        """
        denominator = other.real ** 2 + other.imaginary ** 2
        result_real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        result_imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(result_real, result_imaginary)
