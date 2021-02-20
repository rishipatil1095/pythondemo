# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
n = int(input())
flag = 0
for i in range(n):
    b = set(map(int, input().split()))
    c = a.union(b)
    if len(a) > len(b):
        big = a
        small = b
    else:
        small = a
        big = b

    c = big.union(small)
    if len(c) == len(big):
        if len(big) > len(small):
            flag = True
        else:
            flag = False
            break
    else:
        flag = True
        break

print(flag)
