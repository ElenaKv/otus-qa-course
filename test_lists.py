"""
Проверить, что тип данных - список
Вывести результат на печать
"""


def test_if_data_is_list(lists):
    assert type(lists) == list
    print("====================")
    print("It is " + str(type(list)))


"""
Проверить:
- число 1 есть в списке, вывести результат на печать
- длина списка - 3,
- тип второго элемента списка - словарь,
- список не пустой
"""


def test_if_instanse_in_list(lists):
    for x in lists:
        if x == 1:
            break
    assert 1 in lists
    assert len(lists) == 3
    assert type(lists[2]) is dict
    assert lists != []
    print("====================")
    print("1 presents in list")
