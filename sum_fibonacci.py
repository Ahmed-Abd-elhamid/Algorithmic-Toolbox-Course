def fibNum(n):
    if n <= 0:
        return 0

    a, b = 0, 1
    sum = a + b
        
    for i in range(2,n+1):
        c = (a+b)%10
        a = b
        b = c
        sum += c

    return sum%10

size =int(input()) #take the size
print(fibNum(size))