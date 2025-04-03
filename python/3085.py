def check_candy():
    """
    가로와 세로 방향으로 연속된 같은 색 사탕의 최대 개수를 계산하는 함수
    현재 상태의 보드를 기준으로 가장 긴 연속된 사탕의 길이를 반환함
    """
    max_cnt = 0  # 최대로 연속된 사탕 개수를 저장할 변수

    # 가로 방향 검사
    for i in range(N):  # 각 행마다 반복
        cnt = 1  # 연속된 사탕 개수를 세기 위한 변수 (초기값 1)
        for j in range(1, N):  # 각 열을 두 번째 열부터 끝까지 검사
            if candy_color[i][j] == candy_color[i][j-1]:  # 이전 사탕과 같은 색이라면
                cnt += 1  # 연속된 개수 증가
            else:
                max_cnt = max(max_cnt, cnt)  # 최댓값 갱신
                cnt = 1  # 연속 끊기면 1로 초기화
        max_cnt = max(max_cnt, cnt)  # 마지막 열까지 도달한 후 한 번 더 확인

    # 세로 방향 검사
    for j in range(N):  # 각 열마다 반복
        cnt = 1  # 연속된 사탕 개수 초기화
        for i in range(1, N):  # 각 행을 두 번째 행부터 끝까지 검사
            if candy_color[i][j] == candy_color[i-1][j]:  # 위쪽 사탕과 같다면
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)

    return max_cnt  # 계산된 최댓값 반환
# 보드 크기 입력
N = int(input())  # 정수 N: 보드 크기 (N x N)

# 보드 상태 입력
candy_color = [list(input()) for _ in range(N)]  # 각 줄의 문자열을 리스트로 변환하여 2차원 리스트로 저장

max_candies = 0  # 결과로 출력할 최대 사탕 개수

# 모든 가능한 위치에서 인접한 사탕 교환
for i in range(N):
    for j in range(N):

        # 오른쪽 사탕과 교환 (가로 교환)
        if j + 1 < N and candy_color[i][j] != candy_color[i][j+1]:  # 범위 내 & 서로 다른 색
            candy_color[i][j], candy_color[i][j+1] = candy_color[i][j+1], candy_color[i][j]  # 교환
            max_candies = max(max_candies, check_candy())  # 현재 상태에서 최대 사탕 수 계산
            candy_color[i][j], candy_color[i][j+1] = candy_color[i][j+1], candy_color[i][j]  # 원래 상태로 되돌리기

        # 아래쪽 사탕과 교환 (세로 교환)
        if i + 1 < N and candy_color[i][j] != candy_color[i+1][j]:
            candy_color[i][j], candy_color[i+1][j] = candy_color[i+1][j], candy_color[i][j]  # 교환
            max_candies = max(max_candies, check_candy())  # 최대 사탕 수 갱신 시도
            candy_color[i][j], candy_color[i+1][j] = candy_color[i+1][j], candy_color[i][j]  # 원상 복구

# 결과 출력
print(max_candies)
