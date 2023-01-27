# 사용자가 입력한 숫자의 각 자릿수를 더해 출력하는 sum_of_digit를 작성하라.      단, 반복문을 활용하지 않는 코드로 작성하라.      
# 단, 반복문을 활용한 방법과 반복문을 활용하지 않은 방법을 두가지 모두 작성하라. 

num = input()
sum_ = 0
num_dic=[]


for i in num:
    num_dic.append(i)

print(num_dic) # ['3', '9', '0', '6']
