# 입력: 가로(C), 세로(R)
C, R = map(int, input().split())
K = int(input())

# K가 좌석 수를 초과하면 0 출력
if K > C * R:
    print(0)
else:
    # 좌석 배열 초기화
    matrix = [[0] * C for _ in range(R)]
    
    # 방향: 상, 우, 하, 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    # 시작 위치: 좌측 하단
    r, c = R - 1, 0
    dir = 0  # 초기 방향: 상
    num = 1  # 현재 번호

    while True:
        matrix[r][c] = num  # 번호 배정

        if num == K:
            # 좌표 출력 (1부터 시작)
            print(c + 1, R - r)
            break

        # 다음 위치 계산
        nr = r + dr[dir]
        nc = c + dc[dir]

        # 범위 밖이거나 이미 배정된 경우 방향 전환
        if not (0 <= nr < R and 0 <= nc < C) or matrix[nr][nc] != 0:
            dir = (dir + 1) % 4
            nr = r + dr[dir]
            nc = c + dc[dir]

        r, c = nr, nc  # 위치 이동
        num += 1  # 번호 증가