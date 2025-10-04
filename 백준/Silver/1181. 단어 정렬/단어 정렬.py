import sys
N = int(input())
words = [sys.stdin.readline().strip() for _ in range(N)]
words = sorted(set(words), key=lambda x: (len(x), x))
for i in range(len(words)):
    print(words[i])