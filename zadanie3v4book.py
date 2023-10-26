class Book:#создаем класс
    def __init__(self,author,name,by,year,pages):#конструктор
        self.author = author
        self.name = name
        self.by = by
        self.year = year
        self.pages = pages#инициализируем все эти параметры

    def print_info(self):#функция print_info
        print(f"Автор: {self.author}")
        print(f"Название: {self.name}")
        print(f"Издательство: {self.by}")
        print(f"Год издания: {self.year}")
        print(f"Количество страниц: {self.pages}")#вывод информации