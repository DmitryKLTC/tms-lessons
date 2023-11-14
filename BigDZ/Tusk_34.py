def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0
print(compare(100, 200))
print(compare(200, 100))
print(compare(10, 10))