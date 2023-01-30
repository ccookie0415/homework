# 카쉐어링 서비스는 요금을 다음과 같이 계산한다.
# A.    대여는 10분 단위로 가능하다.
# B.    대여 요금 : 10분당 1,200원
# C.    보험료 : 30분당 525원 (50분을 빌리면, 1시간으로 계산)
# D.   주행 요금 : km당 170원 (주행 요금은 100km가 넘어가면, 넘어간 부분에 대하여 할인이 50% 적용)
# 예) 160km를 달렸으면, 170*100 + 85*60
# 양의 정수인 대여시간(분)과 주행거리를 받아 계산 결과를 반환하는 함수 fee()를 작성하시오.
# 참고 함수 math.ceil 

import math


class CarSharing:
        
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance
       
    def rent(self):
        rent_price = math.ceil(self.time // 10) * 1200
        return rent_price
        
    def insurance(self):
        insurance_price = math.ceil(self.time // 30) * 525
        return insurance_price
        
    def drive(self):
        if self.distance <= 100:
            drive_price = self.distance * 170
        elif self.distance > 100:
            drive_price = 17000 + ((self.distance-100) * 85)
        return drive_price
    
    def fee(self):
        print(self.rent() + self.insurance() + self.drive())

car1 = CarSharing(600,50)
car1.fee()

car2 = CarSharing(600,110)
car2.fee()

# fee(600, 50) #=> 91000
# fee(600, 110) #=> 10
