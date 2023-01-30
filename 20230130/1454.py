# 아래 코드와 같이 국적을 출력할 수 있는 클래스 Nationality를 작성하시오

class Nationality:
    
    def __init__(self,country):
        self.country = country
        
    def __str__(self):
        return f"나의 국적은 {self.country}"    

korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국


