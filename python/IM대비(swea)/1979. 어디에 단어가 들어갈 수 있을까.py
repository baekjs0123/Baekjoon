T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        sum_puzzle = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                sum_puzzle += 1
            if j == N - 1 or puzzle[i][j] == 0:
                if sum_puzzle == K:
                    ans += 1
                sum_puzzle = 0

    for i in range(N):
        sum_puzzle = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                sum_puzzle += 1
            if j == N - 1 or puzzle[j][i] == 0:
                if sum_puzzle == K:
                    ans += 1
                sum_puzzle = 0
    print(f'#{tc} {ans}')

