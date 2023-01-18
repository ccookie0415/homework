# 1.  문자열 배열을 받아 애너그램 단위로 그룹핑하는 함수 group_anagrams을 작성하여라.


# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 
# from collections import defaultdict
words = ['eat','tea','tan','ate','nat','bat']

# def groupAnagrams(self, strs):
#     ana_group = {}
#     for s in strs:
#         sorted_s = ''.join(sorted(s))
#         ana_group[sorted_s] = ana_group.get(sorted_s, []) + [s]
#     return ana_group.values()

# def groupAnagrams(word_list):
#     Anagram_list = []
#     for word in word_list:
#         sorted_s = ''.join(sorted(s))
#         Anagram_list[sorted_s] = Anagram_list.get(sorted,[]) + [s]
#     return Anagram_list.values()

# print(groupAnagrams(word_list))

# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         dic = defaultdict(list)
        
#         for s in strs:
#             dic[''.join(sorted(s))].append(s)
#         return dic.values()

def group_anagrams(words):
    anagrams = {}
    
    for word in words:
        sorted_word = sorted(word)
        key = ''.join(sorted_word)
    
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
            
    return list(anagrams.values())
print(group_anagrams(words))