# 김코딩이 일하고 있는 박물관에 도둑이 들었다. 
# 박물관 입구와 출구에 센서가 있다. 
# 센서는 지나가는 사람이 누구인지 인지하여 방문자를 기록한다. 
# 입장 기록은 entry_record list에, 퇴장 기록은 exit_record list에 
# 아래처럼 정리 되어 있다. 주어진 조건으로 분석하여 수상한 사람을 분별하라.
# 많이 방문한 사람이 도둑일 가능성이 높다. 
# 가장 많이 입장한 세 사람을 찾아 출력하라.
# 입장 횟수와 퇴장 횟수의 차이가 0이어야 정상이다. 
# 횟수의 차이가 있을 경우 정말 수상하다. 
# 입장 횟수와 퇴장 횟수가 같지 않은 사람을 분별하여 출력하라.
# 제약 조건: collection 모듈의 Counter 객체를 활용해야 한다.

from collections import Counter

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

entry_count = Counter(entry_record)
exit_count = Counter(exit_record)

# entry_count key-value값 뽑아내기

def max_entry(entry_count):
    entry_count = sorted(entry_count.items(), key = lambda item: item[1], reverse=True)[:-5]
    for name_count in entry_count:
        a, b = name_count
        print(f'{a} {b}회')

def find_thief(entry_count, exit_count):
    more_entry = entry_count - exit_count
    more_exit = exit_count - entry_count
    more_entry_result = list(zip(more_entry.keys(),more_entry.values()))
    more_exit_result = list(zip(more_exit.keys(),more_exit.values()))
    
    for thief in more_entry_result:
        a, b = thief
        print(f'{a}은 입장 기록이 {b}회 더 많아 수상합니다.')
    for thief2 in more_exit_result:
        c, d = thief2
        print(f'{c}은 퇴장 기록이 {d}회 더 많아 수상합니다.')


print('입장 기록 많은 Top3')
max_entry(entry_count)
print('\n출입 기록이 수상한 사람')
find_thief(entry_count, exit_count)

