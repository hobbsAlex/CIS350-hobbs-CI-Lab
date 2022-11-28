def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def divide_numbers(a, b):
    return a / b

def multiply_numbers(a, b):
    return a * b
    
def larger_number(a, b):
    if a > b:
        return a
    return b

def smaller_number(a, b):
    if a < b:
        return a
    return b


if __name__ == "__main__":
    print("Adding:", add_numbers(2,4))
    print("Subtracting:", subtract_numbers(9,2))