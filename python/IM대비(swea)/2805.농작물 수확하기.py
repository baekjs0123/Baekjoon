T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    center = N // 2
    farm_value = 0
    for i in range(N):
        farm_value += farm[i][center]
        if i <= center:
            for j in range(1, i + 1):
                farm_value += farm[i][center - j]
                farm_value += farm[i][center + j]
        else:
            for j in range(1, N - i):
                farm_value += farm[i][center - j]
                farm_value += farm[i][center + j]
    print(f'#{tc} {farm_value}')