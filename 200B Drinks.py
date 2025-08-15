n=int(input())
l=list(map(int,input().split(" ")))
for i in range(len(l)):
    l[i]/=100
print((sum(l)/n)*100)