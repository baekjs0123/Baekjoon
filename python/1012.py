# 유효성 검사
def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M
# 스택을 이용한 dfs
def dfs_stack(start_r, start_c):
    stack = [(start_r, start_c)]
    # 스택이 빌 때까지 반복
    while stack:
        # 스택에서 하나 꺼내기
        r, c = stack.pop()
        if field[r][c] == 1:
            field[r][c] = 0  # 방문한 배추는 0으로 표시
            # 델타 방향 순회
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                # 유효성 검사를 통과하고 배추가 있으면 스택에 추가
                if is_valid(nr, nc) and field[nr][nc] == 1:
                    stack.append((nr, nc))

T = int(input())
for tc in range(1, T + 1):
    # M: 가로 길이, N: 세로 길이, K: 배추 갯수
    M, N, K = map(int, input().split())
    # 밭 지도
    field = [[0] * M for _ in range(N)]
    # 배추 좌표
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    # 델타 방향
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0
    # 밭 지도를 순회하면서 배추가 있는 위치를 찾아서 dfs 호출
    for r in range(N):
        for c in range(M):
            # 배추가 있는 위치를 찾았으면 배추 갯수 증가
            if field[r][c] == 1:
                dfs_stack(r, c)
                cnt += 1
    print(cnt)
