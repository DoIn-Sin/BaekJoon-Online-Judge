string = (list(input()))
count, word = 0, 0

if len(string) == 0:
        word -= 1
        
for empty in string:

    if (count != 0 and count != (len(string)-1)) and empty == ' ':
        word += 1
    elif len(string) == 1 and empty == ' ':
        word -= 1
    count += 1
    
print(word+1)