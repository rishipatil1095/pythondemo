def GCD(a,b):
    if a > b:
        big,small =  a,b
    else:
        big,small = b,a

    if big%small == 0:
        return small
    else:
        while 1:
            rem = big%small
            if rem == 0:
                return small
            big = small
            small = rem


result = GCD(60,96)
print(result)