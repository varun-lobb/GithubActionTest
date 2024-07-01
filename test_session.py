import pytest
from session import add_numbers

#check if it properly adds positive numbers
def test_add_positive():
    assert add_numbers(1,2) == 3


#check if it properly adds zero
def test_add_zero():
    assert add_numbers(1,0) == 1


#check for negative numbers
def test_add_negative():
    assert add_numbers(4, -10) == -6

    
#check if it produces error 
def test_add_string_expects_exception():
    with pytest.raises(TypeError):
        add_numbers(5,'Test String')

