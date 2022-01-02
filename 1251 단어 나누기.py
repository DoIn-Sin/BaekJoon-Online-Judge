voca = input()
result = []

for word_first_idx in range(len(voca)-2):
    for word_second_idx in range(word_first_idx+1, len(voca)-1):
        for word_third_idx in range(word_second_idx+1, len(voca)):
            voca_case = voca[:word_second_idx][::-1] + voca[word_second_idx:word_third_idx][::-1] + voca[word_third_idx:][::-1]
            result.append(voca_case)
            
print(min(result))
    