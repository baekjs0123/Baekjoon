def is_valid(s, i):
        return s[i] == 'O' and (i != 0 and s[i - 1] != 'O') or (i == 0 and s[i] == 'O')



T = int(input())
for tc in range(T):
    s = input()
    score = 0
    count = 0
    for i in range(len(s)):
        if is_valid(s, i):
            count += 1
            score += count
        elif s[i] == 'O' and s[i-1] == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)

