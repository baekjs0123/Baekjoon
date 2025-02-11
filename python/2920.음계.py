sound = list(map(int, input().split()))
result = ''
cnt = 0
for i in range(len(sound)):
    if sound[i] == i + 1:
        cnt += 1
        result = 'ascending'
    elif sound[i] == len(sound) - i:
        cnt -= 1
        result = 'descending'
    
if cnt == 8:
    print(result)
elif cnt == -8:
    print(result)
else:
    print('mixed')

   