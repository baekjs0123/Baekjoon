# K : 1m^2당 참외 갯수
K = int(input())
# dirs_lens: 방향과 길이를 리스트로 저장
dirs_lens = [list(map(int, input().split())) for _ in range(6)]
"""
접근법
최대 가로,세로 길이를 구해서 큰 직사각형의 넓이를 구하고 작은 사각형의 넓이를 구해서 빼준다.
그 후 단위면적당 참외 갯수를 곱해서 답을 도출한다.
"""

max_width = 0 # 최대 가로길이 담을 변수
max_width_idx = 0 # 최대 가로 길이 인덱스 번호 담을 변수
max_height = 0 # 최대 세로길이 담을 변수
max_height_idx = 0 # 최대 세로 길이 인덱스 번호 담을 변수

# dirs_lens길이만큼 반복을 돌면서 각 방향 d와 길이length를 뽑아서 최대값을 찾는다. 
for i in range(len(dirs_lens)):
    d, length = dirs_lens[i][0], dirs_lens[i][1]
    # d가 동,서 방향일때가 가로
    if d == 1 or d == 2:
        if max_width < length:
            max_width = length
            max_width_idx = i # 최대 길이일때 인덱스 번호 저장
    
    # d가 남,북 방향일때가 세로
    if d == 3 or d == 4:
        if max_height < length:
            max_height = length
            max_height_idx = i # 최대 길이일때 인덱스 번호 저장
# 작은 사각형의 가로 길이는 큰 사각형의 가로길이 인덱스 번호로 부터 + 3에 6으로 나눈 나머지 인덱스이다.
sub_width = dirs_lens[(max_width_idx + 3) % 6][1]
# 작은 사각형의 세로 길이는 큰 사각형의 세로길이 인덱스 번호로 부터 + 3에 6으로 나눈 나머지 인덱스이다.
sub_height = dirs_lens[(max_height_idx + 3) % 6][1]

area = max_width * max_height - sub_width * sub_height
ans = area * K
print(ans)