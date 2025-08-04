num=input()
final=[]
for x in num:
    if x in "1234567890":
        final.append(x)
final.sort()
print("+".join(final))
