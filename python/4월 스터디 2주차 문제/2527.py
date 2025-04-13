# 테스트 케이스 4번 반복
for tc in range(4):
    # 한 줄에 8개의 정수 입력받아서 각각 변수에 저장
    # 첫 번째 직사각형: lectangle1_x1, lectangle1_y1, lectangle1_x2, lectangle1_y2
    # 두 번째 직사각형: lectangle2_x1, lectangle2_y1, lectangle2_x2, lectangle2_y2
    lectangle1_x1, lectangle1_y1, lectangle1_x2, lectangle1_y2, lectangle2_x1, lectangle2_y1, lectangle2_x2, lectangle2_y2 = map(int, input().split())

    # 결과 저장할 변수 초기화
    code = ''

    # 1. 공통부분이 없는 경우 ('d')
    # 두 직사각형이 전혀 겹치지 않는 경우 판단
    # 한 직사각형이 다른 직사각형의 왼쪽, 오른쪽, 위쪽, 아래쪽에 완전히 위치하는 경우
    if (lectangle1_x2 < lectangle2_x1 or  # 첫 번째 직사각형이 두 번째 직사각형의 왼쪽에 있음
        lectangle2_x2 < lectangle1_x1 or  # 두 번째 직사각형이 첫 번째 직사각형의 왼쪽에 있음
        lectangle1_y2 < lectangle2_y1 or  # 첫 번째 직사각형이 두 번째 직사각형의 아래에 있음
        lectangle2_y2 < lectangle1_y1):   # 두 번째 직사각형이 첫 번째 직사각형의 아래에 있음
        code = 'd'

    # 2. 점에서 만나는 경우 ('c')
    # 두 직사각형이 한 점에서만 만나는 경우 판단
    # 각 직사각형의 꼭짓점이 일치하는 경우
    elif ((lectangle1_x2 == lectangle2_x1 and lectangle1_y2 == lectangle2_y1) or  # 오른쪽 위 꼭짓점이 같음
          (lectangle1_x2 == lectangle2_x1 and lectangle1_y1 == lectangle2_y2) or  # 오른쪽 아래 꼭짓점이 같음
          (lectangle1_x1 == lectangle2_x2 and lectangle1_y1 == lectangle2_y2) or  # 왼쪽 아래 꼭짓점이 같음
          (lectangle1_x1 == lectangle2_x2 and lectangle1_y2 == lectangle2_y1)):   # 왼쪽 위 꼭짓점이 같음
        code = 'c'

    # 3. 선분에서 만나는 경우 ('b')
    # 두 직사각형이 한 변에서 만나는 경우 판단
    # 한 변이 일치하고 나머지 좌표가 겹치는 경우
    elif ((lectangle1_x2 == lectangle2_x1 or lectangle1_x1 == lectangle2_x2) or  # 수직 변이 같음
          (lectangle1_y2 == lectangle2_y1 or lectangle1_y1 == lectangle2_y2)):   # 수평 변이 같음
        code = 'b'

    # 4. 직사각형으로 겹치는 경우 ('a')
    # 위의 세 가지 경우에 해당하지 않으면 두 직사각형은 면적으로 겹치는 경우
    else:
        code = 'a'

    print(code)
