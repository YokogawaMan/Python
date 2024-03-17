import datetime


class Logger:
    """
        Класс Logger предназначен для логирования сообщений в файл.

        Attributes:
            filename (str): Имя файла для записи логов.
    """

    def __init__(self, filename):
        """
            Конструктор класса Logger.

            Parameters:
                filename (str): Имя файла для записи логов.
        """
        self.filename = filename

    def log(self, message):
        """
            Метод log используется для записи сообщений в лог-файл.

            Parameters:
                message (str): Сообщение для записи в лог.

            Returns: None.
        """
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(f'-- [{datetime.datetime.now().replace(microsecond=0)}] -- {message}\n')

    def log_error(self, error_message):
        """
            Метод log_error используется для записи сообщений об ошибках в лог-файл.

            Parameters:
                error_message (str): Сообщение об ошибке для записи в лог.

            Returns: None.
        """
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(f'-- [{datetime.datetime.now().replace(microsecond=0)}] -- ERROR: {error_message}\n')
