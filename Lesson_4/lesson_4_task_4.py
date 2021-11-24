import sys
import utils

if __name__ == '__main__':
    program, *argv = sys.argv
    if not len(argv):
        print('Add currency code')
    else:
        current = argv[0]
        result = utils.currency_rates(current, float)
        if result != None:
            print(f'Курс {current} равен {result:.4f}р')
        else:
            print(f'None')
