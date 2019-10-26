import pytest

"""
Список фикстур

"""
@pytest.fixture(scope="class")
def strings():
    data = "I would like to write tests like you!"
    return data


@pytest.fixture(scope="function")
def dicts():
    data = {"2": "One", "3": "Two"}
    return data


@pytest.fixture(scope="function")
def function_fixture():
    x = 5
    print("X = " + str(x))
    return x


@pytest.fixture()
def sets():
    a = set("hello")
    a.clear()


@pytest.fixture()
def tuples():
    tpl_1 = (1,2,3)
    tpl_2 = tpl_1
    return tpl_1, tpl_2



