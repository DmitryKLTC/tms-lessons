def generate_natural_cubes(n:int):
    lst =[i**3 for i in range(n)]
    return lst
print(generate_natural_cubes(12))