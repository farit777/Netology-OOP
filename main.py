from classes.classes import Lecturer, Reviewer, Student

# Создание экземпляров классов
lecturer1 = Lecturer("Иван", "Иванов", ["Python", "Git"])
lecturer2 = Lecturer("Петр", "Петров", ["Python", "Java"])

reviewer1 = Reviewer("Анна", "Сидорова", ["Python", "Git"])
reviewer2 = Reviewer("Мария", "Кузнецова", ["Java", "Git"])

student1 = Student("Руой", "Эман", ["Python"], ["Введение в программирование"])
student2 = Student("Саша", "Сидорова", ["Git"], ["Основы программирования"])

# Выставление оценок
reviewer1.review_homework(student1, "Python", 10)
reviewer1.review_homework(student1, "Python", 9)
reviewer2.review_homework(student2, "Git", 8)

lecturer1.add_grade("Python", 8)
lecturer1.add_grade("Python", 9)
lecturer2.add_grade("Java", 10)

# Печать информации о студентах, лекторах и ревьюерах
print("Поверяющие:")
print(reviewer1)
print(reviewer2)
print("\nЛекторы:")
print(lecturer1)
print(lecturer2)
print("\nСтуденты:")
print(student1)
print(student2)

# Функция для подсчета средней оценки за домашние задания по курсу
def average_homework_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.homework_grades:
            total_grades.extend(student.homework_grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Функция для подсчета средней оценки за лекции по курсу
def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Примеры использования функций
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("\nСредние оценки:")
print("Средняя оценка за домашние задания по Python:", average_homework_grade(students, "Python"))
print("Средняя оценка за лекции по Python:", average_lecturer_grade(lecturers, "Python"))