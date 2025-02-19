S = input()
'''
접근법
s의 a가 처음 등장하는 위치 b가 처음 등장하는위치... z가 처음 등장하는 위치를
공백으로 출력
아스키코드를 활용하여 a ~ z개 만큼 반복을 돌며
각 알파벳이 등장하는 인덱스 번호를 출력한다.
'''
lst = []
duplication = []
for i in range(97,123):
    for j in range(len(S)):
        if S[j] in duplication:
            continue            
        if i == ord(S[j]):
            lst.append(j)
            duplication.append(S[j])
    if chr(i) not in S:
        lst.append(-1)
        
print(*lst)
                    