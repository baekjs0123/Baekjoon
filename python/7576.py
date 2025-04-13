from collections import deque

# 유효성 검사
def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M

def min_days_to_ripe_tomatoes(M, N, box):
    """
    모든 토마토가 익는 데 필요한 최소 일수를 계산하는 함수.

    매개변수:
    M (int): 상자의 가로 칸 수.
    N (int): 상자의 세로 칸 수.
    box (list of list of int): 토마토의 상태를 나타내는 2차원 리스트.
                               1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없는 칸.

    반환값:
    final_day: 모든 토마토가 익는 데 필요한 최소 일수.
         만약 모든 토마토가 이미 익어있다면 0을 반환하고,
         일부 토마토가 끝내 익지 못하면 -1을 반환합니다.
    """
    # 방향 벡터: 상(-1,0), 하(1,0), 좌(0,-1), 우(0,1)
    dr = [-1, 1, 0, 0]  # 행(row) 변화량
    dc = [0, 0, -1, 1]  # 열(column) 변화량
    
    # BFS를 위한 큐 초기화 및 익은 토마토의 위치 저장
    queue = deque()
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                queue.append((r, c, 0))  # (행, 열, 날짜) 형태로 저장
    
    final_day = 0  # 모든 토마토가 익는 데 걸리는 최소 일수
    
    # BFS 수행
    while queue:
        r, c, days = queue.popleft()  # 큐에서 하나의 요소를 꺼냄
        final_day = max(final_day, days)  # 최대 일수 갱신
        
        # 현재 위치의 상하좌우 인접한 칸을 확인
        for i in range(4):
            nr = r + dr[i]  # 새로운 행 좌표
            nc = c + dc[i]  # 새로운 열 좌표
            # 새로운 좌표가 유효하고, 해당 칸에 익지 않은 토마토가 있을 경우
            if is_valid(nr, nc) and box[nr][nc] == 0:
                box[nr][nc] = 1  # 토마토를 익은 상태로 변경
                queue.append((nr, nc, days + 1))  # 큐에 새로운 위치와 날짜를 추가
    
    # 모든 토마토가 익었는지 확인
    for row in box:
        if 0 in row:  # 익지 않은 토마토가 남아있다면
            return -1  # 모든 토마토를 익히는 것이 불가능하므로 -1 반환
    
    return final_day  # 모든 토마토가 익는 데 걸리는 최소 일수 반환

# 입력 받기
M, N = map(int, input().split())  # 상자의 가로(M)와 세로(N) 크기 입력
box = [list(map(int, input().split())) for _ in range(N)]  # 상자의 상태 입력

result = min_days_to_ripe_tomatoes(M, N, box)
print(result)
