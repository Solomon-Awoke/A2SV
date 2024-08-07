t = int(input())
a = []
for _ in range(t):
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    a.append((n, m, b))
out = []
for case in a:
    n, m, b = case
    dig1 = {}
    dig2 = {}
    
    for i in range(n):
        for j in range(m):
            if (i - j) not in dig1:
                dig1[i - j] = 0
            dig1[i - j] += b[i][j]
            
            if (i + j) not in dig2:
                dig2[i + j] = 0
            dig2[i + j] += b[i][j]
    
    max_sum = 0
    for i in range(n):
        for j in range(m):
            current_sum = dig1[i - j] + dig2[i + j] - b[i][j]
            max_sum = max(max_sum, current_sum)
    
    out.append(max_sum)

for res in out:
    print(res)