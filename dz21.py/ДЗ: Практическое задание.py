#Среднее значение по студенту
def calculate_average(grades):
    n = sum(grades)
    counter = 0
    for i in grades:
        counter += 1
    return n/counter

#Находим самого слабого
def get_the_lowers(students):
    return min(students,key=lambda student: calculate_average(student["grades"]))

# Среднее значение по группе
def obtaining_the_groups_average_score(students):
    total_average = sum(calculate_average(student["grades"]) for student in students)
    return total_average / len(students)

#Общий список студентов, баллы и статус
def request_for_student_data(students):
    for student in students:
        name = student["name"]
        average = calculate_average(student["grades"])
        status = "Успешен" if average >= 75 else "Отстаёт"

        print(f"Студент: {name}\nСредний балл: {average:.2f}\nСтатус: {status}\n")


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [98, 90, 98]},
    {"name": "Ron", "grades": [70, 45, 65]},
    {"name": "Drago", "grades": [80, 90, 99]},
    {"name": "Shon", "grades": [10, 40, 23]},
]

the_lowest = get_the_lowers(students)

request_for_student_data(students)

average_score_variable = obtaining_the_groups_average_score(students)
print(f"Общий средний балл группы: {average_score_variable:.2f}")

answer = str(input("Хотите добавить студента? Y = Да\n"))
if answer.lower() == "y":
    students.append({"name": "Shaka", "grades": [90, 97, 93]})

answer_2 = str(input("Хотите удалить самого отстающего студента? Y = Да\n"))
if answer_2.lower() == "y" and the_lowest:
   students = [s for s in students if s["name"] != the_lowest["name"]]

request_for_student_data(students)

average_score_variable = obtaining_the_groups_average_score(students)
print(f"Общий средний балл группы: {average_score_variable:.2f}")
