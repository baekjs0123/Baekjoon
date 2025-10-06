N, M = map(int, input().split())
noListen = []
noSee = []
for i in range(N):
    noListen.append(input())
for j in range(M):
    noSee.append(input())
answer = sorted(set(noListen) & set(noSee))
print(len(answer))
for i in range(len(answer)):
    print(answer[i])