tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Анна', 'Дмитрий', 'Артем'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
tutor_klass_gen = ((tutors[i], klasses[i] if len(klasses) > i else None) for i in range(len(tutors)))
print(type(tutor_klass_gen), *tutor_klass_gen)


