# add, substract, multuply, divide 메소드를 가진 
# Calculator 클래스를 생성하고, 아래의 계산 결과를 출력하라.
# 단, 숫자는 0으로 나눌 수 없다. 
# 이 경우, 예외처리로 0으로 나눌 수 없습니다.를 출력하라.  
# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        try:
            result = self.first / self.second
            return result
    
            if self.second == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            return ("0은 나눌 수 없습니다")
        
        
        
    

        
    # def divideZero(self):
    #     try :
    #         result = self.first / 0
    #         return ZeroDivisionError
    #     except ZeroDivisionError:
    #         raise
    
print(Calculator(1,2).add())
print(Calculator(2,1).sub())
print(Calculator(3,4).mul())
print(Calculator(4,0).div())
    