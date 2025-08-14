t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    iterations = 0
    while True:
        iterations += 1
        dec_idxs = [i for i in range(n) if a[i] > b[i]]
        if not dec_idxs:
            break
        a[dec_idxs[0]] -= 1
        inc_idxs = [i for i in range(n) if a[i] < b[i]]
        if inc_idxs:
            a[inc_idxs[0]] += 1
    print(iterations)
