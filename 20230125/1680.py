#과수원에 농부 한 명이 썩은 과일이 몇 개 들어있는 과일 봉지를 가지고 있다. 
#과일 봉지를 입력받아, 
#썩은 과일 조각들을 모두 신선한 것으로 교체하는 코드를 작성하고 
#리스트 형식으로 출력하시오.
#예를 들어, apple,rottenBanana,apple,RoTTenorange,Orange이라는 
#문자열이 주어진 경우, 
#대체된 리스트는 ['apple', 'banana', 'apple', 'orange', 'orange'] 
#n 만약 리스트가 비어 있는 경우 빈 리스트를 반환한다.
#n 반환된 리스트의 요소는 모두 소문자여야 한다.

fruits = input()
# lst = list(fruits)

lst = list(fruits.split(','))

for i in lst:
    new_lst = []
    i = i.lower()
    if 'rotten' in i:
        i = i.strip('rotten')
    print(i)
#     new_lst.append(i)
# print(new_lst)
    

