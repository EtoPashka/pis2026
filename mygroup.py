groupmates = [
    {
        "name": "Павел",
        "surname": "Османов",
        "exams": ["ПИС", "ОС", "Метрология"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Андрей",
        "surname": "Замахаев",
        "exams": ["ПИС", "АСиПРВ", "МиСПИСиТ"],
        "marks": [3, 5, 5]
    },
    {
        "name": "Илана",
        "surname": "Гагкоева",
        "exams": ["ОПвКИС", "ОС", "МиСПИСиТ"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Дмитрий",
        "surname": "Бочкарев",
        "exams": ["АСиПРВ", "Метрология", "ОПвКИС"],
        "marks": [3, 4, 3]
    },
    {
        "name": "Малинин",
        "surname": "Александр",
        "exams": ["АСиПРВ", "ПИС", "ОС"],
        "marks": [5, 3, 5]
    },
    {
        "name": "Игнатенко",
        "surname": "Александр",
        "exams": ["Метрология", "МиСПИСиТ", "ОПвКИС"],
        "marks": [4, 4, 4]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(15),
          u"Экзамены".ljust(35), u"Оценки".ljust(15))

    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(15),
            str(student["exams"]).ljust(35),
            str(student["marks"]).ljust(15)
        )


def filter_students(students, average_mark):
    filtered_students = []

    for student in students:
        average = sum(student["marks"]) / len(student["marks"])

        if average > average_mark:
            filtered_students.append(student)

    return filtered_students


print_students(groupmates)

average_mark = float(input("Введите средний балл для фильтрации: "))

filtered_students = filter_students(groupmates, average_mark)

print("\nСтуденты, средний балл которых выше заданного:")

if filtered_students:
    print_students(filtered_students)
else:
    print("Студенты не найдены.")
