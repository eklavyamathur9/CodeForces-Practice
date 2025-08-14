n, t = map(int, input().split())
L = list(input())
for _ in range(t):
    i = 0
    while i < n - 1:
        if L[i] == 'B' and L[i+1] == 'G':
            L[i], L[i+1] = L[i+1], L[i]
            i += 2
        else:
            i += 1
print(''.join(L))
