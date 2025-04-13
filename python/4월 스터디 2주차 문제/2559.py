# N: 전체 온도 수, K: 연속된 일수
N, K = map(int, input().split())

# 온도 리스트 입력받기
temperatures = list(map(int, input().split()))

# 첫 K일의 합으로 초기화
current_sum = sum(temperatures[:K])
max_sum = current_sum

# 슬라이딩 윈도우로 최대 합 찾기
for i in range(K, N):
    current_sum = current_sum - temperatures[i - K] + temperatures[i]
    max_sum = max(max_sum, current_sum)

print(max_sum)
