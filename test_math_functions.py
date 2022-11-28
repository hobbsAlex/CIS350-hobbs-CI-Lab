from math_functions import *
def test_calc_addition():
    output = add_numbers(2,4)
    assert output == 6
def test_calc_substraction():
    output = subtract_numbers(2, 4)
    assert output == -2
def test_calc_multiply():
    output = multiply_numbers(2,4)
    assert output == 8
#def test_calc_multiply_fail():
    #output = multiply_numbers(2,4)
    #assert output == 16
def test_calc_divide():
    output = divide_numbers(10,2)
    assert output == 5

def test_calc_larger():
    output = larger_number(8,2)
    assert output == 8
def test_calc_smaller():
    output = smaller_number(5,3)
    assert output == 3

def test_calc_larger2():
    output = larger_number(1,-7)
    assert output == 1
def test_calc_smaller2():
    output = smaller_number(-2,-1)
    assert output == -2
