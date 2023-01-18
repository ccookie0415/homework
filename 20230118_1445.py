# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

year = int(input('연도를 입력하세요 : '))
leapcheck = calendar.isleap(year)

while leapcheck:
    print('윤년입니다. 연도를 다시 입력해주세요.')
    year = int(input('연도를 입력하세요 : '))
    leapcheck = calendar.isleap(year)
    if leapcheck == False: # 윤년아닌경우
        print(calendar.calendar(year))
        break
    
if leapcheck == False: # 윤년아닌경우
        print(calendar.calendar(year))
    
year = int(input('연도를 입력하세요 : '))
month = int(input('월을 입력하세요 : '))
day = int(input('일을 입력하세요 : '))
if calendar.weekday(year,month,day) == 0:
    print("경고 월요일입니다")
    print({'년' : year, '월' : month, '일' : day, '요일' : '월요일'})
elif calendar.weekday(year,month,day) == 1:
    print({'년' : year, '월' : month, '일' : day, '요일' : '화요일'})
elif calendar.weekday(year,month,day) == 2:
    print({'년' : year, '월' : month, '일' : day, '요일' : '수요일'})
elif calendar.weekday(year,month,day) == 3:
    print({'년' : year, '월' : month, '일' : day, '요일' : '목요일'})
elif calendar.weekday(year,month,day) == 4:
    print({'년' : year, '월' : month, '일' : day, '요일' : '금요일'})
elif calendar.weekday(year,month,day) == 5:
    print({'년' : year, '월' : month, '일' : day, '요일' : '토요일'})
elif calendar.weekday(year,month,day) == 6:
    print({'년' : year, '월' : month, '일' : day, '요일' : '일요일'})
