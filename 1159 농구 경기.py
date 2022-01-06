person_num = int(input())
name = []
first_name = []
for lines in range(person_num):
    name.append(list(input()))

for a in range(person_num):
    for b in range(person_num):
        if b == 0 :
            first_name.append(name[a][b])

same_count= {}
for word in first_name:
    try: same_count[word]+= 1
    except: same_count[word]=1

result = []
for key, val in same_count.items():
    if val >= 5:
        result.append(key)

result.sort()
if len(result) != 0 :
    for i in result:
        print(i, end='')
else:
    print("PREDAJA")