import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print(-1, 2)
    else:
        res = []
        for i in range(1, n+1):
            if i % 2 == 1:
                res.append(-1)
            else:
                res.append(3)
        print(*res)
