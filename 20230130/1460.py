# i. 입력된 수가 짝수라면 2로 나눈다.  
# ii.입력된 수가 홀수라면 3을 곱하고 1을 더한다. 
# iii. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.

# 위 작업을 몇 번이나 반복해야하는지 반환하는 함수 collatz()를 작성하시오 
# (단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환하시오.)

# collatz(6) #=> 8
# collatz(16) #=> 4
# collatz(27) #=> 111
# collatz(626331) #=> -1

class cal:
    
    def __init__(self,num):
        self.num = num
           
    count = 0
    
    def calc(self):
        cal.count = 0
        while True:
            if self.num == 1:
                return cal.count
            
            elif self.num % 2 == 0:
                self.num = self.num / 2
                cal.count += 1
                
            elif self.num % 2 == 1:
                self.num = self.num * 3 + 1
                cal.count += 1
                
            if cal.count >= 500:
                return -1
                
    def collatz(self):
        print(cal.calc(self))
        
num1 = cal(6)
num1.collatz()

num2 = cal(16)
num2.collatz()

num3 = cal(27)
num3.collatz()

num4 = cal(626331)
num4.collatz()