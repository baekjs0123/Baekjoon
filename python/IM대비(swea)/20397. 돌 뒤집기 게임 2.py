T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    default_stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        for k in range(1, j + 1):
            if 0 <= i - k and i + k < N:
                if default_stones[i - k] == default_stones[i + k]:
                    if default_stones[i - k]:
                        default_stones[i - k] = 0
                        default_stones[i + k] = 0
                    else:
                        default_stones[i - k] = 1
                        default_stones[i + k] = 1
            else:
                break

    print(f"#{tc}", *default_stones)
