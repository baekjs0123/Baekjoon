T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_sum = 0
    min_sum = 3600
    for r in range(N):
        for c in range(N):
            sum_point = matrix[r][c]
            for d in range(4):
                for n in range(1, N):
                    nr = r + dr[d] * n
                    nc = c + dc[d] * n
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_point += matrix[nr][nc]
            if max_sum < sum_point:
                max_sum = sum_point
            if min_sum > sum_point:
                min_sum = sum_point
    print(f'#{tc} {max_sum - min_sum}')



