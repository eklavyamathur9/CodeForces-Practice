n=list(map(int,input().split()))
a=list(map(int,input().split()))
s=0
x=a[n[1]-1]
for m in a:
    if m>=x and m>0:
        s+=1
print(s)

