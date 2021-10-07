import sys

sum_list = []
with open('bakery.csv', 'r', encoding='utf-8') as f:
    sum = f.readline().replace('\n', '')
    while sum:
        sum_list.append(sum)
        sum = f.readline().replace('\n', '')

len_sum_list = len(sum_list)
if len_sum_list == 0:
    sys.exit('Продаж нет')
if len(sys.argv) == 1:
    bon = [bon for bon in sum_list]
    print(bon)
elif len(sys.argv) == 2:
    start = int(sys.argv[1]) - 1
    if start > len_sum_list:
        sys.exit('Error number')
    bon = [bon for bon in sum_list[start:]]
    print(bon)
elif len(sys.argv) == 3:
    start = int(sys.argv[1]) - 1
    stop = int(sys.argv[2])
    if start > len_sum_list:
        sys.exit(f'Значение превышает:  {len_sum_list}')
    if start > stop or start == stop:
        sys.exit(f'Error srart number')
    bon = [bon for bon in sum_list[start:stop]]
    print(bon)
else:
    sys.exit('Введите python show_sales.py')


