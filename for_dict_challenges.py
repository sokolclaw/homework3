# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = [name['first_name'] for name in students]
used_names = []
for name in names:
    if name in used_names:
        continue 
    count = names.count(name) 
    print(f'{name}: {count}')
    used_names.append(name)

def find_popular_name(people):
    names = [name['first_name'] for name in people]
    count_max = 0
    name_max = ''
    for name in names:
        count = names.count(name) 
        if count < count_max:
            continue
        count_max = count
        name_max = name
    return name_max

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

print(f'Самое частое имя среди учеников: {find_popular_name(students)}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for number, students in zip(range(1, len(school_students) + 1), school_students):
    # students = [student for student in school_students[i]]
    print(f'Самое частое имя в классе {number}: {find_popular_name(students)}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

def who_in_class(people, males):
    girls = 0
    boys = 0
    names = []
    for student in people['students']:
        names.append(student['first_name'])
        if males[student['first_name']]:
            boys += 1
        else:
            girls += 1
    return {'girls': girls, 'boys': boys}

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


for classroom in school:
    girls = who_in_class(classroom, is_male)['girls']
    boys = who_in_class(classroom, is_male)['boys']
    print(f"Класс {classroom['class']}: девочки {girls}, мальчики {boys}")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
girls_max, girls_max_class = 0, ''
boys_max, boys_max_class = 0, ''
for classroom in school:
    girls = who_in_class(classroom, is_male)['girls']
    boys = who_in_class(classroom, is_male)['boys']
    if girls_max < girls:
        girls_max = girls
        girls_max_class = classroom['class']
    if boys_max < boys:
        boys_max = boys
        boys_max_class = classroom['class']
print(f'Больше всего мальчиков в классе {boys_max_class}\nБольше всего девочек в классе {girls_max_class}')