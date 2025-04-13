from collections import deque

def is_valid(r, c):
    """
    주어진 좌표 (r, c)가 지도 범위 내에 있는지 확인하는 함수
    """
    return 0 <= r < h and 0 <= c < w

def bfs(start_x, start_y, map):
    """
    시작 지점 (start_x, start_y)에서 BFS를 수행하여 최장 거리를 계산하는 함수

    매개변수:
    start_x, start_y: 시작 지점의 좌표
    map: 지도를 나타내는 2차원 리스트

    반환값:
    max_distance: 시작 지점으로부터 가장 먼 지점까지의 거리
    """
    # 상하좌우 이동을 위한 방향 벡터
    dr = [-1, 1, 0, 0]  # 행 방향 이동: 위, 아래
    dc = [0, 0, -1, 1]  # 열 방향 이동: 왼쪽, 오른쪽

    # BFS를 위한 큐 초기화 및 시작 지점 추가
    queue = deque([(start_x, start_y)])

    # 방문 여부 및 거리를 저장하는 2차원 리스트 초기화
    visited = [[-1] * w for _ in range(h)]
    visited[start_x][start_y] = 0  # 시작 지점의 거리는 0

    max_distance = 0  # 최장 거리를 저장할 변수

    # 큐가 빌 때까지 반복
    while queue:
        r, c = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        current_distance = visited[r][c]  # 현재 위치까지의 거리

        # 네 방향으로 이동 시도
        for i in range(4):
            nr = r + dr[i]  # 새로운 행 위치
            nc = c + dc[i]  # 새로운 열 위치

            # 새로운 위치가 유효한 범위 내에 있고, 육지('L')이며, 아직 방문하지 않았다면
            if is_valid(nr, nc) and map[nr][nc] == 'L' and visited[nr][nc] == -1:
                visited[nr][nc] = current_distance + 1  # 거리를 갱신
                queue.append((nr, nc))  # 큐에 새로운 위치 추가
                max_distance = max(max_distance, visited[nr][nc])  # 최장 거리 갱신

    return max_distance  # 최장 거리 반환

# 지도 크기 입력 받기
h, w = map(int, input().split())

# 지도 정보 입력 받기
map = [list(input()) for _ in range(h)]

max_distance = 0  # 전체 최장 거리를 저장할 변수

# 지도 전체를 순회하며 각 'L' 지점에서 BFS 실행
for i in range(h):
    for j in range(w):
        if map[i][j] == 'L':  # 현재 위치가 육지라면
            max_distance = max(max_distance, bfs(i, j, map))  # 최장 거리 갱신

print(max_distance)  # 최장 거리 출력
