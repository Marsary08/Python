def thesaurus(*args):
    name = {}
    for i in sorted(args):
        letter = i[0]
        if letter in name:
            name[letter] += [i]
        else:
            name[letter] = [i]

    return name


print(thesaurus("Игорь", "Анна", "Антонина", "Павел", "Петр", "Роман", "Валерия", "Яна"))
