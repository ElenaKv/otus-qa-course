"""
Проверить, что обе переменных ссылаются на один и тот же объект
Вывести результат на печать

"""


def test_tuples(tuples):
    print(id(tuples[0]), id(tuples[1]))
    assert id(tuples[0]) == id(tuples[1])
