#   문제
# 끝말잇기 단어의 리스트가 주어졌을 때, 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.
# 	조건
# 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for idx in range(1, len(words)):
    print(idx) # 지금의 나
    print(words[idx-1][-1], words[idx][0]) #직전 사람
    
    if words[idx-1][-1] != words[idx][0]:
        print('실패', idx, words[idx])
        break
        
    #처음부터~나까지
    elif words[idx] in words[:idx]:
        print('실패', idx, words[idx])
        break
    
# words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
# flag = False
# for idx in range(1, len(words)):
#     print(idx)
#     # 지금의 나

#     if words[idx-1][-1] != words[idx][0]:
#         print('실패', idx, words[idx])
#         flag = True
#     else:
#         for sub_idx in range(idx):
#             pre_word = words[sub_idx]
#             me_word = words[idx]
#             if pre_word == me_word:
#                 print('실패', idx, words[idx])
#                 flag = True
#                 break
#     if flag:
#         break
