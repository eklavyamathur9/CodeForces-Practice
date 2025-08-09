t = int(input().strip())
for _ in range(t):
    data = input().split()
    n = int(data[0])
    x = int(data[1]) - 1  
    s = input().strip()
    left_segment = s[:x]  
    right_segment = s[x+1:]  
    left_length = len(left_segment)
    right_length = len(right_segment)
    has_left_wall = '#' in left_segment
    has_right_wall = '#' in right_segment
    if left_length == 0:
        cost_left = 1
    else:
        if has_left_wall:
            cost_left = left_length + 1
        else:
            cost_left = left_length
            
    if right_length == 0:
        cost_right = 1
    else:
        if has_right_wall:
            cost_right = right_length + 1
        else:
            cost_right = right_length
            
    ans = min(cost_left, cost_right)
    print(ans)
