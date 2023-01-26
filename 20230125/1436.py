# 10 미만의 자연수에서 2과 7의 배수를 구하면 2,4,6,7,8이다. 
# 이들의 총합은 27이다.1000미만의 자연수에서 2,7의 배수의 총합을 구하라.

number = 1000

def find_multiple(number):
    sum_ = 0
    for i in range(1,number):
        if i % 2 == 0 or i % 7 == 0:
            sum_ = sum_ + i
    return sum_

print(find_multiple(number))