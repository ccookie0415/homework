# 생성되는 총 페이지의 수를 출력하는 프로그램 작성

total = int(input("게시글의 총 갯수를 입력하세요 : "))
page = int(input("한 페이지에 필요한 게시글 수를 입력하세요 : "))

total_page = total / page
print(total_page)