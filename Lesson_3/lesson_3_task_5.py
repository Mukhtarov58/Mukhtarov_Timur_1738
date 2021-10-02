import random

def get_jokes(nice_jokes):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    words_joke = [nouns] + [adverbs] + [adjectives]
    result = []
    for _ in range(nice_jokes):
        jokes = ''
        for word in words_joke:
             random_word = random.choice(word)
             jokes += f'{random_word}'
        result.append(jokes[:-1])
    return result
print(get_jokes(4))
print(get_jokes(3))
