# i.초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
# ii. bark() 메서드를 호출하면 개는 짖을 수 있다.    
# iii.클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
# 개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
# 개가 죽으면 num_of_dogs의 값이 1 감소한다.
# iv. get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다

class dog:
    
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self,name,species):
        self.name = name
        self.species = species
        dog.num_of_dogs += 1
        dog.birth_of_dogs += 1
        
        
    def bark(self):
        print(f"{self.name} : 멍멍!")
        
    def death(self):
        dog.num_of_dogs -= 1
        return dog.num_of_dogs
    
    def get_status():
        print(dog.birth_of_dogs, dog.num_of_dogs)
    
        
dog1 = dog("쿠키","포메")
dog2 = dog("멍멍","시츄")

dog.get_status()