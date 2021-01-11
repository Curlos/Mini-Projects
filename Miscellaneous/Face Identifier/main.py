def recur(n):
    if(n <= 10):
        print(f"*2 : {n * 2}")
        return n * 2
    else:
        print(f"Greater than 10: {n}")
        return recur(recur(n/3))


print(recur(27))
