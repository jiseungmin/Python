# 코딩스터디 모임 날짜

from random import randint


day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+str(day)+"일로 정하였습니다.")

url = "https://naver.com"
my_str = url.replace("https://", "")
my = my_str.replace(".com", "")
print("{0}{1}{2}!".format(my[:3], len(my), my.count("e")))
