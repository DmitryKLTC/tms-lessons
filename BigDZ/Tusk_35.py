def filter_negative_numbers(numbers):
    new_numbers = []
    for num in numbers:
        if num >= 0:
            new_numbers.append(num)
    return new_numbers
print(filter_negative_numbers([-4, -2, 1, 2, 3]))
print(filter_negative_numbers([4, 5, 12, -3, 0, -100]))