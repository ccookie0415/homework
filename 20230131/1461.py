# 김해피는 구슬치기 대회에 참가하였다. 
# 모든 인원은 참가 번호를 부여받는데, 
# 자신과 같은 참가 번호를 가진 사람과 구슬치기 게임을 진행하여야 한다.
# 단, 반드시 짝이 없는 한 명의 깍두기가 존재한다. 
# 참가자들의 참가 번호 정보가 리스트로 주어질 때, 깍두기의 참가 번호를 출력하시오.

# A.참가자 번호는 1번부터 시작합니다.
# B.깍두기는 한 명만 존재합니다.
# C.깍두기를 제외한 모든 참가자는 자신의 짝(자신과 같은 수)이 존재합니다.



class Game:
   
    def __init__(self,participants):
        self.participants = participants
        
    def remainder(self):
        lst_1 = []
        lst_2 = []
        self.participants.sort()
        
        for i in range(0,len(self.participants)):
            if i % 2 == 1:
                lst_1.append(self.participants[i])
        
            elif i % 2 == 0:
                lst_2.append(self.participants[i])
           
        for j in lst_2:
            if j not in lst_1:
              print(j)
        
participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
lst = Game(participants)
lst.remainder()

# participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
# participants.sort()
# lst_1 = []
# lst_2 = []

# for i in range(0,len(participants)):
#     if i % 2 == 1:
#         lst_1.append(participants[i])
#     elif i % 2 == 0:
#         lst_2.append(participants[i])
        
# for j in lst_2:
#     if j not in lst_1:
#         print(j)
