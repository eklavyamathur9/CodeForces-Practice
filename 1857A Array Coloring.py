t=int(input())
for _ in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    c=0
    for i in lst:
        c+=i
    if c%2==0:
        print("YES")
    else:
        print("no")  