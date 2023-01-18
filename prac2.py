# import calendar

# year = int(input('연도를 입력하세요 : '))

# # day = {'월요일 : 0', '화요일 : 1', '수요일 : 2', '목요일 : 3', '금요일 : 4', '토요일 : 5', '일요일 : 6'}

# def isLeapYear(year):
#     if calendar.isleap(year) == True:  #True = 윤년 , Fasle = 평년
#         print("윤년입니다. 연도를 다시 입력해주세요.")
#         year = int(input('연도를 입력하세요 : '))
#         print(calendar.calendar(year, w=2, l=1, c=6, m=3))
#     if calendar.isleap(year) == False:
#         year = int(input('연도를 입력하세요 : '))
#         month = int(input('월을 입력하세요 : '))
#         day = int(input('일을 입력하세요 : '))
#         if calendar.weekday(year,month,day) == 0:
#             print("경고 월요일입니다")
#             print({'년' : year, '월' : month, '요일' : '월요일'})
#         elif calendar.weekday(year,month,day) == 1:
#             print({'년' : year, '월' : month, '요일' : '화요일'})
#         elif calendar.weekday(year,month,day) == 2:
#             print({'년' : year, '월' : month, '요일' : '수요일'})
#         elif calendar.weekday(year,month,day) == 3:
#             print({'년' : year, '월' : month, '요일' : '목요일'})
#         elif calendar.weekday(year,month,day) == 4:
#             print({'년' : year, '월' : month, '요일' : '금요일'})
#         elif calendar.weekday(year,month,day) == 5:
#             print({'년' : year, '월' : month, '요일' : '토요일'})
#         elif calendar.weekday(year,month,day) == 6:
#             print({'년' : year, '월' : month, '요일' : '일요일'})

# isLeapYear(year)

day = {0 : '월요일', 1 : '화요일', 2 : '수요일', 3 : '목요일', 4 : '금요일', 5 : '토요일', 6 : '일요일'}
print(day.keys())