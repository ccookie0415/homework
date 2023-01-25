# 작물과 가격이 함께 있는 리스트가 존재할 때, 가장 높은 가격을 가지고 있는 작물의 이름을 출력하라.
# 단, 작물의 이름을 직접 입력하여 출력하지 않는다.

grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

#
def max_cost_grain(grain_lst):
    grain_dic = dict(grain_lst)
    
    for key,value in grain_dic.items():
        if value == max(grain_dic.values()):
            return key
        
print(max_cost_grain(grain_lst))