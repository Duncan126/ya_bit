import pytest


def add_sum(a, b):
    return a + b


# маркируем как смоук-тест
@pytest.mark.smoke
def test_add():
    assert add_sum(2, 3) == 5, 'сумма не равна ожидаемой'


# маркируем как регрессионный тест
@pytest.mark.regression
def test_type_result():
    assert isinstance(add_sum(2, 3), int), \
        'не соответствует ожидаемому типу данных' 
    
def test_addition_with_fixture(sample_numbers):
    a, b, expected = sample_numbers
    assert a + b == expected, f"{a} + {b} должно быть {expected}" 


def test_data_processing(temporary_data):
    """
    Тест использует данные из фикстуры и проверяет их обработку
    """
    print("Начало теста - данные:", temporary_data)

    # Проверяем сумму
    assert sum(temporary_data) == 15

    # Проверяем количество элементов
    assert len(temporary_data) == 5

    # Модифицируем данные (это безопасно - после теста они очистятся)
    temporary_data.append(6)
    print("Данные изменены:", temporary_data)
   
    print("Тест завершён")
