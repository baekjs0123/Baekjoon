T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    # H : 호텔의 층 수
    # W : 각 층의 방 수
    # N : 몇번째 손님?
    # N번째 손님이 머물 층을 계산합니다.
    # N을 H로 나눈 나머지가 해당 손님의 층이 됩니다.
    floor = N % H

    # N번째 손님이 머물 방 번호를 계산합니다.
    # N을 H로 나눈 몫에 1을 더한 값이 방 번호가 됩니다.
    room_number = N // H + 1

    # 만약 floor가 0이라면, 이는 N이 H의 배수임을 의미합니다.
    # 이 경우 손님은 꼭대기 층에 배정되어야 하므로 floor를 H로 설정하고,
    # room_number를 1 감소시킵니다.
    if floor == 0:
        floor = H
        room_number -= 1

    # 최종 방 번호를 출력합니다.
    # 층 수는 두 자리로, 방 번호는 두 자리로 표현되므로,
    # 층 수에 100을 곱하고 방 번호를 더하여 출력합니다.
    print(f"{floor * 100 + room_number}")
            

