import random#импорт рандома
from задание2 import Student, byGPA_key#импорт Student, byGPA_key из задания2
students = [
    Student(
        input('Введите фамилию и имя студента: '),
        input('Введите номер группы: '),#запрашиваем пользователя ввести данные
        [random.randint(1, 10) for _ in range(5)]#5 рандомных оценок
    )
    for _ in range(10)#оценки от 1 до 10
]
students_sort = sorted(students, key=byGPA_key)#сортируем студентов
for student in students_sort:#
    student.print_info()#выводим инфо студентов