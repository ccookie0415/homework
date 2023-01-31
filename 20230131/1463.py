# 클래스를 활용하여 PublicTransport을 표현하시오.
# A. PublicTransport는 이름 name 과 요금 fare을 인스턴스 속성으로 가진다.
# B. 탑승get_in, 하차get_off하는 메서드를 필요로 한다.
# i. 이 때, passenger의 수를 받는다.
# C. 현재 탑승자 수를 알 수 있어야 한다.
# D. 최종 수익을 계산하는 메소드 profit 은 요금과 전체 탑승자 수를 곱해서 계산한다.

class PublicTransport:
    
    def __init__(self,name,fare):
        self.name = name
        self.fare = fare
    total_passenger= 0
    
    def get_in(self,in_passenger):
        self.in_passenger = in_passenger
        self.total_passenger += in_passenger
        return self.total_passenger
    
    def get_off(self,out_passenger):
        self.out_passenger = out_passenger
        self.total_passenger -= out_passenger 
        return self.total_passenger
    
    # def profit(self):
        # total_passenger = self.in_person - self.out_person
        # total_fare = self.fare * total_passenger
        # return total_fare
    
person1 = PublicTransport('임혜진2', 600)
person2 = PublicTransport('임혜진2', 600)
person3 = PublicTransport('임혜진3', 600)

print(PublicTransport.total_passenger)

# print(PublicTransport.get_in)