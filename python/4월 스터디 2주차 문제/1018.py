# 체스판의 두 가지 가능한 패턴을 기준으로 다시 칠해야 하는 칸의 수를 계산하는 함수
def count_repaints(board, start_row, start_col):
    # 두 가지 체스판 패턴: 시작 색상이 'W'인 경우와 'B'인 경우
    patterns = [['W', 'B'], ['B', 'W']]
    min_repaints = 50000
    # 두 가지 패턴에 대해 각각 계산
    for pattern in patterns:
        repaint_count = 0  # 현재 패턴에서 다시 칠해야 하는 칸의 수를 0으로 초기화
        for i in range(8):  # 8행
            for j in range(8):  # 8열
                # 현재 위치에서 기대되는 색상을 계산
                expected_color = pattern[(i + j) % 2]
                # 실제 색상과 기대되는 색상이 다르면 다시 칠해야 함
                if board[start_row + i][start_col + j] != expected_color:
                    repaint_count += 1
        # 두 패턴 중에서 더 적은 다시 칠해야 하는 칸의 수를 선택
        min_repaints = min(min_repaints, repaint_count)

    return min_repaints  # 최소 다시 칠해야 하는 칸의 수 반환

# 입력 처리
N, M = map(int, input().split())  # N: 행의 수, M: 열의 수
board = [list(input()) for _ in range(N)]  # 체스판 정보를 2차원 리스트로 저장

min_cnt = 50000

# 체스판에서 가능한 모든 8x8 부분을 검사
for i in range(N - 7):  # 행의 시작 위치
    for j in range(M - 7):  # 열의 시작 위치
        cnt = count_repaints(board, i, j)  # 현재 8x8 부분에서 다시 칠해야 하는 칸의 수 계산
        min_cnt = min(min_cnt, cnt)  # 최소값 갱신

print(min_cnt)  # 결과 출력
