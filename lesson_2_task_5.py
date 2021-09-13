




price = [10, 2.5, 45, 78.5, 69.8, 7, 98, 10.23, 15.1, 12, 1, 2.2]
price_correct = []
for i in price:
    rub = int(i)
    kop = round((i-rub) * 100)
    price_correct.append(f'{rub} руб {kop} коп' )
print(sorted(price_correct, reverse=True))

#сортировка пока не получается. понимаю, что чрез def и lambda но пока не пойму
