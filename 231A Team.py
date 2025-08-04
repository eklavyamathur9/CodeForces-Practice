def countq(n):
    c = 0
    for _ in range(n):
        p, v, t = map(int, input().split())
        if p + v + t >= 2:
            c += 1
    return c
 
n = int(input())
print(countq(n))
