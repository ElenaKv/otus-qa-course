import pytest
"""
Это session фикстура
она возвращает список из трех элементов
"""


@pytest.fixture(scope="session")
def lists():
    data = [1, "One", {1: "Name"}]
    return data
