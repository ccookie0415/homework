# 문자열을 전달 받아 해당 문자열의 정중앙 문자를 출력하시오. 
# 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 출력하라.

str_ = (input())
lst = list(str_)
div_ = len(str_) // 2

if len(str_) % 2 == 1:
    print(lst[div_])

elif len(str_) % 2 == 0:
    print(lst[div_-1], lst[div_])