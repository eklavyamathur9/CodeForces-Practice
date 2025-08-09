'''n=int(input())
l=list(map(int,input().split()))
total=sum(l)
c=0
for x in range(len(l)):
    if total>l[-1]:
        c+=1
        l.pop()
print(c)'''
n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
t = sum(l)
ts = 0
c = 0
for x in l:
    ts += x
    c += 1
    if ts > t - ts:
        break
print(c)
