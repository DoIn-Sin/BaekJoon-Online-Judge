sen = input()
sen = sen.upper()
count={}
lists = sen
for i in lists:
    try: count[i] += 1
    except: count[i]=1
maxstr = []
for k,v in count.items():
    if max(count.values()) == v:
        maxstr.append(k)
if len(maxstr) == 1:
    print(maxstr[0])
else:
    print('?')
