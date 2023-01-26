# 여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아 
# key는 혈액형의 종류, value는 사람 수인 dictionary를 만드시오.

blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

def dic_blood(blood_types):
    count_A = 0
    count_B = 0
    count_AB = 0
    count_O = 0
    key = []
    for blood in blood_types:
        key.append(blood)
        if blood == 'A':
            count_A = count_A + 1
        elif blood == 'B':
            count_B = count_B + 1
        elif blood == 'AB':
            count_AB = count_AB + 1
        else :
            count_O = count_O + 1
    value = [count_A, count_AB, count_B, count_O]
    print(list(set(key)).sort())
    print(value)    
        
print(dic_blood(blood_types))