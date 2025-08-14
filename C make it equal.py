import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        k = int(data[index])
        index += 1
        S = list(map(int, data[index:index + n]))
        index += n
        T_list = list(map(int, data[index:index + n]))
        index += n
        
        count_S = {}
        for x in S:
            r = x % k
            if r == 0:
                key = 0
            else:
                key = min(r, k - r)
            count_S[key] = count_S.get(key, 0) + 1
        
        count_T = {}
        for x in T_list:
            r = x % k
            if r == 0:
                key = 0
            else:
                key = min(r, k - r)
            count_T[key] = count_T.get(key, 0) + 1
        
        if count_S == count_T:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()