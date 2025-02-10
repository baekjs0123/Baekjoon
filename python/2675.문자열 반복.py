T = int(input())

for tc in range(1, T + 1):

    R , S = map(str, input().split())
    R = int(R)
    P = []
    for i in range(len(S)):
        P.append(S[i] * R)
    
    for i in P:
        print(i, end='')
    print()