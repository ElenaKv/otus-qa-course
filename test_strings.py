"""
Вывести на печать длину строки,
проверить, что длина строки не превышает 40
проверить, что строка не пустая
проверить, что строка начинается с заглавной буквы
"""


class TestString:

    def test_string_is_shorter_than_forty(self, strings):
        print("I would like to write tests like you! has length - " + str(len(strings)))
        assert len(strings) < 40
        assert strings != ()
        assert strings[0].isupper() is True
