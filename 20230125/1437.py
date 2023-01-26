# 두 개의 정수 n과 m이 주어졌을 때, 
# 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 
# 별(*) 문자를 이용하여 출력하시오.

n = int(input('가로 길이를 입력하세요 : '))
m = int(input('세로 길이를 입력하세요 : '))


for i in range(m):
    for j in range(n):
        print('*', end ='')
    print()