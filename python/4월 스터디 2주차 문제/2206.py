from collections import deque

# 입력을 빠르게 받기 위한 설정

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs():
    # 큐 생성 및 초기 위치 추가 (x, y, 벽 부순 여부)
    queue = deque()
    queue.append((0, 0, 0))  # 시작점에서 벽을 부수지 않은 상태

    # 방문 배열 초기화
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1  # 시작점 방문 처리

    while queue:
        x, y, wall = queue.popleft()

        # 도착 지점에 도달한 경우
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        # 네 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아닌 경우
                if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    queue.append((nx, ny, wall))
                # 벽인 경우, 아직 벽을 부수지 않았다면
                elif graph[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    queue.append((nx, ny, 1))

    # 도달할 수 없는 경우
    return -1

# 입력 처리
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# BFS 실행 및 결과 출력
print(bfs())