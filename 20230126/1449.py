# 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 
# count_vowels 함수를 작성하시오.

word = input()
box = 'aeiou'

def count_vowels(word):
    count = 0
    for i in word:
        for j in box:
            if i in j:
                count += +1
    return count
            

print(count_vowels(word))

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3

