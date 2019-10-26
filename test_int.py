"""
Проверить, что переменная - целое число
"""


def test_if_data_is_int(function_fixture):
    assert isinstance(function_fixture, int) is True
