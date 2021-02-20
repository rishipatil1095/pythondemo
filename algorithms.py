# linear search
'''pos = -1

def search(lst,n):
    global pos
    for i in range(len(lst)):
        if lst[i] == n:
            pos = i+1
            return True

    return False


lst = [1, 4, 7, 3, 9, 6]
n = 9

if search(lst, n):
    print(n, "found at", pos)
else:
    print(n, "not found")'''

'''
#binary search
pos = -1

def search(lst,n):
    global pos
    l = 0
    u = len(lst)-1
    while 1 <= n:
        mid = (l+u)//2
        if lst[mid] == n:
            pos = mid
            return True
        elif mid > n:
            u = mid-1
        else:
            l = mid+1

    return False

lst = [1,7,34,69,344,678,5678,10011]
n = 5678

if search(lst, n):
    print(n, "found at", pos+1)
else:
    print(n, "not found")
'''
#bubble sort
'''
def srt(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] >= lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

lst = [5,2,8,4,9,3,11,7]
srt(lst)
print(lst)
'''
#selection sort

def sel_srt(lst):
    for i in range(len(lst)-1):
        min_pos = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min_pos]:
                min_pos = j

        temp = lst[i]
        lst[i] = lst[min_pos]
        lst[min_pos] = temp

lst = [5,2,8,4,9,3,11,7]
sel_srt(lst)
print(lst)

