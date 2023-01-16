# 사용자에게 입력받은 수의 각 자리수의 합을 구하라

s = input('숫자를 입력해주세요 : ')
s_sum = sum(list(map(int,str(s))))
print(s_sum)