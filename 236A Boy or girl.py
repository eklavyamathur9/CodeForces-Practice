word=input()
c=0
l=[]
for x in word:
    if x not in l:
        l.append(x)
w="".join(l)
n=len(w)
if n%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
