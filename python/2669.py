arr = [[0] * 100 for _ in range(100)]

for i in range(4):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            if arr[j][k] == 0:
                arr[j][k] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 0:
            continue
        else:
            cnt += 1
print(cnt)
