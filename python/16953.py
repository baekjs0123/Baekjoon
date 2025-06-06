def transform(A, B):
    """
    함수 설명:
    주어진 정수 A를 B로 변환하기 위한 최소 연산 횟수를 계산한다.
    가능한 연산은 다음 두 가지이다:
    1. 현재 수에 2를 곱한다.
    2. 현재 수의 가장 오른쪽에 1을 추가한다.
    
    매개변수:
    A (int): 시작 정수 (1 ≤ A < B ≤ 10^9)
    B (int): 목표 정수
    
    반환값:
    cnt: A를 B로 변환하는 데 필요한 최소 연산 횟수에 1을 더한 값.
         변환이 불가능한 경우 -1을 반환한다.
    """
    cnt = 1  # 연산 횟수를 저장하는 변수. 초기값은 1.
    while B != A:  # B가 A와 같아질 때까지 반복한다.
        if B < A:
            # B가 A보다 작아지면 변환이 불가능하므로 -1을 반환한다.
            return -1
        if B % 10 == 1:
            # B의 가장 오른쪽 숫자가 1이면, 10으로 나누어 1을 제거한다.
            B //= 10
        elif B % 2 == 0:
            # B가 2로 나누어 떨어지면, 2로 나눈다.
            B //= 2
        else:
            # 위의 두 조건이 모두 해당되지 않으면 변환이 불가능하므로 -1을 반환한다.
            return -1
        cnt += 1  # 연산을 수행했으므로 count를 1 증가시킨다.
    return cnt  # 최종적으로 연산 횟수를 반환한다.

A, B = map(int, input().split())

print(transform(A, B))
