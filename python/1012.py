from pprint import pprint

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

T = int(input())
for tc i
    # M: 가로 길이, N: 세로 길이, K: 배추 갯수
    M, N, K = map(int, input().split())
    # 밭 지도
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        # 배추 좌표
        X, Y = map(int, input().split())
        field[Y][X] = 1
    # 델타 방향
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    cnt = 0
    for i in range(4):
        for r in range(N):
            for c in range(M):
                nr = r + dr[i]
                nc = c + dc[i]
                if field[r][c] == 1:
                    cnt += 1
                    if is_valid(nr, nc) and field[nr][nc] == 1:
                        

                    

