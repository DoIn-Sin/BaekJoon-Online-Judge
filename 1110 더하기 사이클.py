num = int(input())
check_num = num
count, new_num = 0, 0

if num == 0:
    count += 1
else:
    while new_num != check_num:
        temp = num//10+num%10
        new_num = (num%10)*10+temp%10
        num = new_num
        count += 1
    
print(count)