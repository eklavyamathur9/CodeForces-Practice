t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    fixed = [x for x in arr if x != -1]
    if not fixed:
        print("YES")
    else:
        if min(fixed) == max(fixed) and min(fixed) != 0:
            print("YES")
        else:
            print("NO")
