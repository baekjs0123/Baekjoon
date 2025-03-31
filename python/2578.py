# 빙고판 입력 (5x5)
board = [list(map(int, input().split())) for _ in range(5)]
# 호출된 숫자들을 1차원 리스트로 변환 (총 25개)
called_numbers = []
for _ in range(5):
    called_numbers.extend(list(map(int, input().split())))
    
def check_bingo(board):
    cnt = 0
    # 행 체크
    for row in board:
        if all(num == 0 for num in row):
            cnt += 1
    # 열 체크
    for j in range(5):
        if all(board[i][j] == 0 for i in range(5)):
            cnt += 1
    # 주 대각선 체크
    if all(board[i][i] == 0 for i in range(5)):
        cnt += 1
    # 부 대각선 체크
    if all(board[i][4-i] == 0 for i in range(5)):
        cnt += 1
    return cnt

call_count = 0
for num in called_numbers:
    call_count += 1
    # 빙고판에서 해당 숫자를 0으로 변경
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
    # 빙고 개수 확인
    if check_bingo(board) >= 3:
        print(call_count)
        exit(0)  # 프로그램 종료
