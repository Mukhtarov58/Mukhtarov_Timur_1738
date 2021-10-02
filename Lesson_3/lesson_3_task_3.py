def thesaurus(*args):
    dict_result = {}
    for name in args:
        name_list = []
        first_letter = name[0]
        if dict_result.get(first_letter):
            if isinstance(dict_result[first_letter], list):
                name_list = dict_result[first_letter]
            else:
                name_list.append(dict_result[first_letter])
            name_list.append(name)
            dict_result[first_letter] = name_list
        else:
            dict_result[first_letter] = name
    return dict_result
print(thesaurus('Мария', 'Маша', 'Павел', 'Петр', 'Иван', 'Илья'))

