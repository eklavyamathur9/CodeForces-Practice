word = input()
prev = ''
count = 0
found = False
for x in word:
    if x == prev:
        count += 1
    else:
        count = 1
    prev = x
    if count >= 7:
        found = True
        break
if found:
    print('YES')
else:
    print('NO')
