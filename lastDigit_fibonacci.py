def fibNum(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2,n+1):
        arr.append( (arr[i-1] + arr[i-2])%10 )
        if i > 4:
            arr[i-3] = 0
            arr[i-4] = 0
    return arr[n]

size = int(input()) #take the size
print(fibNum(size))