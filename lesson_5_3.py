from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А']

result = (i for i in zip_longest(tutors, classes) if len(tutors) > len(classes))

print(result)
print(*islice(result, 9))
print(list(islice(result, 3)))
