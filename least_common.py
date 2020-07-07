def gcd(a,b):
    if b == 0:
        return a
    rem = a%b
    return gcd(b,rem)

def lcm(a,b): 
    return int((a*b) / gcd(a,b))

x, y = map(int, input().split())
print(lcm(x, y))