import pyfiglet as fig


class Title:
    """
        Класс, отвечающий за вывод заголовка калькулятора.

        Parameters: None.
    """

    def __init__(self):
        """
            Инициализирует объект класса Title и выводит заголовок калькулятора.

            Parameters: None.
        """
        print("\033[1;36m", "=" * 100)
        title = "P y t h o n\nC a l c u l a t o r"
        print("\033[1;36m", fig.figlet_format(title, font="slant"))
        print("\033[1;36m", fig.figlet_format("Made by Isaev Anton", font="term"))
