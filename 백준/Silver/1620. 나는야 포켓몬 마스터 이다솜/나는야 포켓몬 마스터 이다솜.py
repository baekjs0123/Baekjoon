import sys
input = sys.stdin.readline
N, M = map(int, input().split())

numToName = {}
nameToNum = {}

for i in range(1, N + 1):
    name = input().strip()
    numToName[i] = name
    nameToNum[name] = i

result = []

for _ in range(M):
    problem = input().strip()
    if problem.isdigit():
        result.append(numToName[int(problem)])
    else:
        result.append(str(nameToNum[problem]))
sys.stdout.write("\n".join(result))