N = int(input())
paper = [[0] * 100 for _ in range(100)]
for i in range(N):
    lx, ly = map(int, input().split())
    for j in range(lx, lx + 10):
        for k in range(ly, ly + 10):
            paper[j][k] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)