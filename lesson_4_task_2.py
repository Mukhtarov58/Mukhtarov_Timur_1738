import requests
import decimal


def currency_rates(current_name, vol_course):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    i_current_name = content.find(f'<CharCode>{current_name}</CharCode>', 0, len(content))
    if i_current_name != 0:
        i_course = content.find('<Value>', i_current_name, len(content)) + len('<Value>')
        i_course_end = content.find('</Value>', i_current_name, len(content))
        course_str = content[i_course:i_course_end].replace(',','.')
        result = vol_course(course_str)
        return result
    else:
        return None, None


if __name__ == '__main__':
    current = 'EUR'
    result = currency_rates(current,  decimal.Decimal)
    if result != None:
        print(f'Курс {current} равен {result:.4f}р')
    else:
        print(f'None')
