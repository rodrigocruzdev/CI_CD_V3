import pytest
from bronze.up2data.read_database import calculate

def test_calculate_area_square():
    assert calculate(2) == 4
    assert calculate(2.5) == 6.25

def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        calculate(-2)

def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        calculate("2")

def test_calculate_area_square_list():
    with pytest.raises(TypeError):
        calculate([2])