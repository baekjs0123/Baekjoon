# for문을 돌려 찍어내는 방법
num = int(input())

for i in range(1, num+1):
    print(' ' * (num - i), end='')
    print('*' * i, end='')
    print()

# 위 코드를 조금 더 간결하게 수정한 버전
num = int(input())

for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * i)


# rjust() 메서드를 활용한 방법
N = int(input())

for i in range(1, N + 1):
    print(('*' * i).rjust(N))
