def open_account():
    print("계좌가 생성되었습니다.")


def deposit(bacne, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(bacne+money))
    return bacne+money


def withdraw(bance, money):  # 출금
    if bance >= money:
        print("{}출금되었습니다. 잔액은 {}".format(money, bance-money))
        return bance - money
    else:
        print("출금이 불가능 합니다. 잔액은{}".format(bance))


def withdraw_night(bance, money):  # 저녁시간 수수료 100원 추가 출금
    a = 100
    print("현재시간은 수수료 {}원이 발생합니다. 잔액은 {}".format(a, bance-money-a))
    return bance-money-a


bance = 5000
bance = deposit(bance, 1000)
bance = withdraw(bance, 1000)
withdraw_night(bance, 500)


# def 기본값 설정

def profile(name, age=17, main_lag="python"):
    print("{}님은 {}살이고 메인 언어는 {}입니다.".format(name, age, main_lag))


profile("유재석")
profile("유재석", 50, "Java")

# def 가변인자


def profile2(name, age, *lang):  # * lang 가변인자로 선언
    print("{}님은 {}살입니다.".format(name, age), end=" ")
    for lag in lang:
        print(lag, end=" ")
    print()


profile2("유재석", 19, "python", "java", "kotlin", "JS")
profile2("정형돈", 19, "java", "c", "C#")

# 전역변수와 지역변수
gun = 10


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("총기함에 있는 총은 {}개 입니다.".format(gun))


checkpoint(2)


def checkpoint2(gun, soldiers):
    gun = gun - soldiers
    print("총기함에 있는 총은 {}개 입니다.".format(gun))
    return gun


checkpoint2(gun, 2)
