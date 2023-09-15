s1 = input()
arr = s1.split()
for i in range(len(arr) - 1):
    print(arr[i], end='...')
print(arr[-1])