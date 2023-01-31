# i. __init__(): 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다.      
# ii. empty(): 스택이 비었다면 True을 반환하고, 그렇지 않다면 False를 반환한다.     
# iii. top(): 스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환한다.     
# iv.  pop(): 스택의 가장 마지막 데이터의 값을 반환하고, 해당 데이터를 삭제한다. 스택이 비었다면 None을 반환한다.      
# v. push(): 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.      
# vi. __repr__: 현재 스택의 요소들을 보여준다.


class Stack:
    def __init__(self):
        self.a =[]
        
    def __len__(self):
        return len(self.a)
    
    def __str__(self):
        return str(self.a)
    
    def empty(self):
        return len(self.a) == 0
    
    def top(self):
        if len(self.a) != 0:
            return self.a[-1]
        elif len(self.a) == 0:
            return None
    
    def pop(self):
        if len(self.a) != 0:
            return self.a.pop(-1)
        else:
            return None
        
    def push(self,x):
        self.a.append(x)
        
    def __repr__(self):
        for i in self.a:
            print (i)
            
        
lst = Stack()
# lst.__init__()
lst.push(8)
lst.push(9)
lst.push(7)
lst.push(10)

print(lst.pop())
print(lst.top())
print(lst.empty())
print(lst.__repr__())
