N, K = map(int, input().split())
Ai = [int(input()) for _ in range(N)]
Ai.sort(reverse=True)
answer = 0
for i in range(N):
    coinCount = 0
    if K > 0 and Ai[i] <= K:
        coinCount = K // Ai[i]
        answer += coinCount
        K -= Ai[i] * coinCount
print(answer)
