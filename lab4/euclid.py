def is_triangle(a, b, c):
    return (a+b > c) and (a+c > b) and (b+c > a)
    
print(is_triangle(2, 2, 4))
