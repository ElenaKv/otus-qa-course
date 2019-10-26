"""
Проверить, что тип данных - словарь
вывести результат на печать
"""


def test_if_data_is_dict(dicts):
    print("====================")
    print("It is " + str(type(dicts)))
    assert type(dicts) == dict


"""
Вывести на печать ключи 
Проверить, что длина словаря - 2
"""


def test_len_list(dicts):
    for key, value in dicts.items():
        print("====================")
        print(str(key) + " is key")

    assert len(dicts.keys()) == 2
