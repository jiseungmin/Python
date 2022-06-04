# 코딩스터디 모임 날짜

from random import randint, shuffle
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+str(day)+"일로 정하였습니다.")

url = "https://naver.com"
my_str = url.replace("https://", "")
my = my_str.replace(".com", "")
print("{0}{1}{2}!".format(my[:3], len(my), my.count("e")))


user = range(1, 21)
user = list(user)
shuffle(user)

print("당첨자발표")
print("치킨 당첨자: {}".format(user[0]))
print("커피 당첨자: {0}".format(user[1:4]))
print("축하합니다.")


def std_weight(height, gender):
    if gender == "남자":
        weight = height/100 * height/100 * 22
    elif gender == "여자":
        weight = height/100 * height/100 * 21

    print("키{}cm 남자의 표준 체중은 {}kg 입니다.".format(height, round(weight, 2)))


std_weight(175, "남자")
