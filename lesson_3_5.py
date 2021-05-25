import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "сонный", "печальный"]


def get_jokes(n, repeat=False):
    """
    Функция возвращает случайные шутки из 3-х списков слов.
    """
    list_jokes = []
    for i in range(n):
        if repeat:
            joke = f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}"
            list_jokes.append(joke)
        else:
            joke = f"{nouns.pop(random.randrange(len(nouns)))} {adverbs.pop(random.randrange(len(adverbs)))} {adjectives.pop(random.randrange(len(adjectives)))}"
            list_jokes.append(joke)
    return list_jokes


print(get_jokes(5, False))
