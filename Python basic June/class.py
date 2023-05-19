class unit:
    # class를 생성하고 초기화하기 위함 init 함수를 선언하고 인자값을 넣어주어 변수선언 ex)marin,tank
    def __init__(self, name, hp, damage):
        self.name = name  # self 초기화
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(name))
        print("체력은 {} 공격력은 {}".format(hp, damage))

    def attack(self, location):  # 클래스안에 메소드는 self를 꼭 넣어야함
        print("{}이 {}방향으로 공격하였습니다.".format(self.name, location))

    def damaged(self, damage):
        print("{}이 {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{}이 죽었습니다.".format(self.name))
        else:
            print("{}이 {}체력이 남았습니다.".format(self.name, self.hp))


marin = unit("마린", 50, 5)
marin.attack("5시")
marin.damaged(25)
marin.damaged(25)
#vicon = "사람"
# vicon.attack("5시") # class 생성자로 생성 안된 변수는 class안 메소드 사용불가

tank = unit("탱크", 150, 50)

wraith1 = unit("레이스", 80, 10)
print("{}가 생성되었습니다. 공격력은{}".format(wraith1.name, wraith1.damage))  # 맴버변수 이용

wraith2 = unit("빼앗긴레이스", 80, 10)
wraith2.cloking = True  # 맴버변수를 생성하여 초기화해서 사용가능

if wraith2 == True:
    print("{}이 클로킹 중입니다.".format(wraith2.name))
else:
    print("{}이 클로킹 중이 아닙니다.".format(wraith2.name))
