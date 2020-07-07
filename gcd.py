def gcd(a,b):
    if b == 0:
        return a
    rem = a%b
    return gcd(b,rem)

x, y = map(int, input().split())
print(gcd(x,y))