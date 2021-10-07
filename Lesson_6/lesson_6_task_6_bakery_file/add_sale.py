import sys

if(len(sys.argv) <= 1):
    sys.exit('Добавить сумму python add_sale.py <сумма>')
sum_bun = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f:
    if not f.write(sum_bun + '\n'):
        print('Error')
    else:
        print(f'{sum_bun} записано')
