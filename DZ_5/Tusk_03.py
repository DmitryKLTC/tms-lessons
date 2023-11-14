def generate_squares(*args):
    lst=[i**2 for i in args]
    return lst
print(generate_squares(1,2,3))