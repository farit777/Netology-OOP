class Mentor:
    def __init__(self, first_name, last_name, courses):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = courses

    def __str__(self):
        return f'Имя: {self.first_name}\nФамилия: {self.last_name}'

class Lecturer(Mentor):
    def __init__(self, first_name, last_name, courses):
        super().__init__(first_name, last_name, courses)
        self.grades = {course: [] for course in courses}

    def add_grade(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)

    def average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        return f'Имя: {self.first_name}\nФамилия: {self.last_name}\nСредняя оценка за лекции: {self.average_grade():.1f}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def __init__(self, first_name, last_name, courses):
        super().__init__(first_name, last_name, courses)

    def review_homework(self, student, course, grade):
        if course in self.courses:
            student.add_homework_grade(course, grade)

class Student:
    def __init__(self, first_name, last_name, courses_in_progress, finished_courses):
        self.first_name = first_name
        self.last_name = last_name
        self.courses_in_progress = courses_in_progress
        self.finished_courses = finished_courses
        self.homework_grades = {course: [] for course in courses_in_progress}

    def add_homework_grade(self, course, grade):
        if course in self.homework_grades:
            self.homework_grades[course].append(grade)

    def average_homework_grade(self):
        total_grades = sum(sum(grades) for grades in self.homework_grades.values())
        total_count = sum(len(grades) for grades in self.homework_grades.values())
        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        return (f'Имя: {self.first_name}\nФамилия: {self.last_name}\n'
                f'Средняя оценка за домашние задания: {self.average_homework_grade():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.average_homework_grade() < other.average_homework_grade()