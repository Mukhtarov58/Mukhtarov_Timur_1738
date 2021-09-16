
list_translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}
def num_translate(num):
    if num.lower() in list_translate:
        if num[0].istitle():
            return list_translate[num.lower()].capitalize()
        else:
            return list_translate[num.lower()]
    else:
        return None


num_user_enter = input('введите число от 1 до 10 на английском:  ')
print(num_translate(num_user_enter))
