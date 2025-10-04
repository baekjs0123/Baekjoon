N, X = map(int, input().split())
numbers = list(map(int, input().split()))
answer = []
for i in range(N):
    if numbers[i] < X:
        answer.append(numbers[i])
print(*answer)