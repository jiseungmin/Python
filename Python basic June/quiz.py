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

    print("키{}cm 남자의 표준 체중은 {:.2f}kg 입니다.".format(height, weight))


std_weight(175, "남자")


for i in range(1, 51):
    file = open("{}주차.txt".format(i), "w", encoding="utf8")
    print("-{} 주자 중간보고-".format(i), file=file)
    print("부서 : ", file=file)
    print("이름 :", file=file)
    print("업무 요약 :", file=file)
    file.close()


class house:
    def __init__(self, location, house_type, price, deal_type, complication_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.comlication_year = complication_year

    def show_detail(self):
        print(self.location, self.house_type,
              self.deal_type, self.price, self.comlication_year)


h1 = house("강남", "아파트", "매매", "10억", "2017년")
h2 = house("마포", "주택", "전세", "7억", "2012년")
h3 = house("송파", "빌라", "매매", "50억", "2010년")
home = []
home.append(h1)
home.append(h2)
home.append(h3)

print("총 {}개의 집이 있습니다.".format(len(home)))
for homes in home:
    homes.show_detail()
