# Dictionary로 이루어진 list를 전달 받아 모든 
# dictionary의 'age' key에 해당하는 value들의 합을 구하시오.

infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

def age_sum(infos):
    sum_ = 0
    for dic in infos:
        sum_ = sum_ + dic['age']
    return sum_    

print(age_sum(infos))