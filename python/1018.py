def is_valid_board(r, c):
    return 0 <= r < M and 0 <= c < N 

def is_valid_temp(r, c):
    return 0 <= r < 8 and 0 <= c < 8

M, N = map(int, input().split()) # M: 세로, N: 가로
board = [list(input()) for _ in range(N)]
min_cnt = 50000
for i in range(M):
    for j in range(N):
        cnt = 0
        if is_valid_board(i + 7, j + 7):
            temp = [row[j:j+8] for row in board[i:i+8]]
            for k in range(8):
                for n in range(8):
                    if is_valid_temp(k+1, n+1) and temp[k][n] == temp[k][n + 1]:
                        if temp[k][n + 1] == 'B':
                            temp[k][n + 1] = 'W'
                        else:
                            temp[k][n + 1] = 'B'
                        cnt += 1
                        
            if min_cnt > cnt:
                min_cnt = cnt
print(min_cnt)

