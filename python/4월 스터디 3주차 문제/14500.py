# 입력 처리
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 방향 벡터(상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False]*M for _ in range(N)]
max_sum = 0

def dfs(r, c, depth, total):
    # depth가 4면 값 갱신 후 종료
    if depth == 4:
        global max_sum
        if total > max_sum:
            max_sum = total
        return

    # 4방향으로 이동
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 범위 검사 및 방문 검사
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True      # 방문 표시
            dfs(nr, nc, depth+1, total + board[nr][nc])
            visited[nr][nc] = False     # 백트래킹

def check_t_shape(r, c):
    """ ㅗ,ㅜ,ㅏ,ㅓ 모양 처리 """
    global max_sum
    center = board[r][c]
    wings = []
    # 인접한 네 칸의 값을 모아둠
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            wings.append(board[nr][nc])

    # 4개 중 3개를 골라 합 계산
    if len(wings) >= 3:
        wings.sort(reverse=True)      # 큰 순으로 정렬
        total = center + sum(wings[:3])
        if total > max_sum:
            max_sum = total

# 모든 칸 순회하며 DFS와 ㅗ 모양 처리
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])     # 일반 모양
        visited[i][j] = False
        check_t_shape(i, j)           # 특별 모양

print(max_sum)
