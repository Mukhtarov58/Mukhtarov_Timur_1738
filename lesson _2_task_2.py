#Необходимо его обработать — обособить каждое целое число
#вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента
#списка,являющегося числом)
#и дополнить нулём до двух целочисленных разрядов:

usl = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

elem = 0
while elem < len(usl):
    plus_elem = usl[elem]
    try:
        int(plus_elem)
        if plus_elem[0] == '+' or plus_elem[0] == '-':
            sign = plus_elem[0]
            plus_elem = plus_elem[1:len(plus_elem)]
        else:
            sign = ''
        usl[elem:elem + 1] = ['"', f'{sign}{plus_elem:0>2}', '"']
        elem += 3
    except ValueError:
        elem += 1
print(usl)

