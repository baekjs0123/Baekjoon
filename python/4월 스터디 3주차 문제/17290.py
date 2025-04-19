def is_valid(r, c):
    return 0 <= r < 10 and 0 <= c < 10

r, c = map(int, input().split())
r -= 1
c -= 1

MAP = [list(input()) for _ in range(10)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 폭탄의 물줄기 표시
after_bomb = [['x'] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if MAP[i][j] == 'o':
            # 폭탄 위치도 안전 구역으로 표시
            after_bomb[i][j] = 'o'
            # 상/하/좌/우 끝까지 표시
            for d in range(4):
                nr, nc = i, j
                while True:
                    nr += dr[d]
                    nc += dc[d]
                    if not is_valid(nr, nc):
                        break
                    after_bomb[nr][nc] = 'o'

# 시작 위치가 이미 안전하다면 0만 출력
if after_bomb[r][c] == 'x':
    print(0)
else:
    # 안전한 칸 목록
    safe_area = [
        (i, j)
        for i in range(10)
        for j in range(10)
        if after_bomb[i][j] == 'x'
    ]
    
    # 맨해튼 거리의 최소값 출력
    min_length = min(abs(r - i) + abs(c - j) for i, j in safe_area)
    print(min_length)