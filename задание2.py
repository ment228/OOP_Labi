import random#импортируем рандом
class Student:#новый класс студент
    def __init__(self, name, group_number, academic_performance):#функция __init__ с параметрами name, group_number, academic_performance
        self.name = name
        self.group_number = group_number
        self.academic_performance = academic_performance
        self.gpa_scores = sum(self.academic_performance) / 5#инициализирует параметры
    def print_info(self):#фунцтя print_info
        print(f'ФИ: {self.name}\n'#вывод имени
              f'  Номер группы: {self.group_number}\n'
              f'  Успеваемость: {self.academic_performance}\n'
              f'  Средний балл: {self.gpa_scores}\n')#вывод остальной информации
def byGPA_key(person):#
    return person.gpa_scores#возвращает ср балл