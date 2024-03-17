from ComplexNumber import ComplexNumber
from Logger import Logger


class UserInterface:
    """
        Класс, представляющий пользовательский интерфейс для калькулятора комплексных чисел.

        Attributes:
            calculator (Calculator): Объект калькулятора, который будет использоваться для выполнения операций.

        Methods:
            input_complex_number(prompt): Запрашивает у пользователя ввод комплексного числа.
            display_result(result): Отображает результат операции.
            run(): Запускает интерфейс для взаимодействия с пользователем.
    """

    def __init__(self, calculator):
        """
            Инициализирует объект UserInterface.

            Parameters:
                calculator (Calculator): Объект калькулятора, который будет использоваться для выполнения операций.
        """
        self.calculator = calculator
        self.logger = Logger("calculator_log.txt")

    def input_complex_number(self, prompt):
        """
            Запрашивает у пользователя ввод комплексного числа.

            Parameters:
                prompt (str): Строка, предназначенная для отображения пользователю перед вводом.

            Returns:
                ComplexNumber: Комплексное число, введенное пользователем.
        """
        print(prompt)
        while True:
            try:
                real = float(input("-- Enter real part: "))
                imaginary = float(input("-- Enter imaginary part: "))
                return ComplexNumber(real, imaginary)
            except ValueError as ex:
                print(f'\033[1;31m{ex}\033[0m')

    def display_result(self, result):
        """
            Отображает результат операции.

            Parameters:
                result (ComplexNumber): Результат операции, который нужно отобразить.
        """
        print(f'\033[1;36m[*] Result:\033[0m {result}')

    def run(self):
        """
            Запускает интерфейс для взаимодействия с пользователем.
        """
        while True:
            num1 = self.input_complex_number("\033[1;36m[*] Enter first complex number\033[0m")
            num2 = self.input_complex_number("\033[1;36m[*] Enter second complex number\033[0m")

            while True:
                operation = input("-- Enter operation [ + ][ - ][ * ][ / ]: ")
                if operation in ['+', '-', '*', '/']:
                    break
                else:
                    print("\033[1;31mInvalid operation! Enter the operation only from the suggested options.\033[0m")

            try:
                if operation == '+':
                    result = self.calculator.add(num1, num2)
                elif operation == '-':
                    result = self.calculator.subtract(num1, num2)
                elif operation == '*':
                    result = self.calculator.multiply(num1, num2)
                elif operation == '/':
                    result = self.calculator.divide(num1, num2)
            except ZeroDivisionError as ex:
                result = ex
                self.logger.log_error(ex)

            self.display_result(result)

            control_question = input('\033[1;36m-- Do you wish to continue? y/n:\033[0m ').lower()

            while control_question not in ['y', 'n']:
                print('\033[1;31mEnter y/n only!\033[0m')
                control_question = input('\033[1;36m-- Do you wish to continue? y/n:\033[0m ').lower()

            if control_question == 'n':
                break
