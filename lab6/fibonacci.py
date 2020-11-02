def fibonacci(upper_bound):
    lst = [0, 1]
    idx = 1
    while True:
        fibo = lst[idx] + lst[idx - 1]
        if fibo >= upper_bound:
            break
        idx += 1
        lst.append(fibo)
    return lst

print(fibonacci(1000))
