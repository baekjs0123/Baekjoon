def is_valid(r, c):
    return 0 <= r < M and 0 <= c < N 

M, N = map(int, input().split()) # M: 세로, N: 가로
board = [list(input()) for _ in range(N)]
min_cnt = 50000
for i in range(M):
    for j in range(N):
        cnt = 0
        temp = board
        for k in range(8):
            for n in range(8):
                if is_valid(k+1, n+1) and temp[k][n] == temp[k][n + 1]:
                    cnt += 1
                    
        if min_cnt > cnt:
            min_cnt = cnt
print(min_cnt)

