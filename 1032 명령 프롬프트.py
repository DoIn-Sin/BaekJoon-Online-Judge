n = int(input())
str1 = list(input())

for i in range(n-1):
    str2 = list(input())
    for j in range(len(str1)):
        if str1[j] != str2[j]:
            str1[j] = '?'
print(''.join(str1))