# 일반 유닛
from random import randint


class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{}(가)이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("[지상유닛이동]")
        print("{}이 {}로 이동합니다. 속도:[{}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{}이 {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{}이 죽었습니다.".format(self.name))
        else:
            print("{}이 {}체력이 남았습니다.".format(self.name, self.hp))

# 공격 유닛


class attackunit(unit):  # 부모클래스 unit에 자식클래스 attackunit이 상속 받음
    def __init__(self, name, hp, damage, speed):
        unit.__init__(self, name, hp, speed)  # unit에 __init__메소드를 상속받음
        self.damage = damage

    def attack(self, location):  # 클래스안에 메소드는 self를 꼭 넣어야함
        print("{}이 {}방향으로 공격하였습니다.".format(self.name, location))

# 다중 상속


class flyable:
    def __init__(self, flyspeed):
        self.flyspeed = flyspeed

    def flying(self, name, location):
        print("{}이 {}로 날아갔습니다.{}속도".format(name, location, self.flyspeed))


class flyingAttackunit(attackunit, flyable):  # 다중 상속
    def __init__(self, name, damage, hp, flyspeed):
        attackunit.__init__(self, name, damage, 0, hp)
        flyable.__init__(self, flyspeed)

    def move(self, location):
        print("[공중유닛이동]")
        # 오버라이딩 부모 클래스의 메소드를, 자식 클래스에서 재정의 하여 사용하는 것을 의미한다.
        self.flying(self.name, location)


class Marin(attackunit):
    def __init__(self):
        attackunit.__init__(self, "마린", 50, 10, 1)

    def steampck(self):
        if self.hp > 10:
            print("마린이 스팀팩을 사용하였습니다.")
        elif self.hp < 10:
            print("피가 부족하여 스팀팩을 사용하지 못하였습니다.")


class tank(attackunit):
    sizmode_Develope = False

    def __init__(self):
        attackunit.__init__(self, "탱크", 140, 100, 3)

    def sizmode(self):
        sizmode = False
        if sizmode == False:
            sizmode = True
            self.damage *= 2
            self.hp /= 2
            print("시즈모드가 실행되었습니다.")
        else:
            sizmode = False
            self.damage /= 2
            self.hp *= 2
            print("시즈모드가 실행되었습니다.")


class wraith(flyingAttackunit):
    def __init__(self):
        flyingAttackunit.__init__(self, "레이스", 60, 300, 5)
        self.clocked = False

    def cloking(self):
        if self.clocked == False:
            self.clocked = True
            print("클로킹을 시작합니다.")
        else:
            self.clocked = False
            print("클로킹이 해제되었습니다.")


def gamestart():
    print("게임이 시작되었습니다.")


def gameover():
    print("플레이어가 나갔습니다.")
    print("Good Game")


# 유닛들 생성
m1 = Marin()
m2 = Marin()
t1 = tank()
t2 = tank()
w1 = wraith()
w2 = wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
attack_units.append(w2)

# 전군이동
for units in attack_units:
    units.move("9시")

# 탱크 시즈모드 개발
sizmode_Develope = True

# 공격 모드 준비
for units in attack_units:
    if isinstance(units, Marin):
        units.steampck()
    if isinstance(units, tank):
        units.sizmode()
    if isinstance(units, wraith):
        units.cloking()

# 전군 공격
for units in attack_units:
    units.attack("9시")

# 전군 피해
for units in attack_units:
    units.damaged(randint(30, 300))

# 게임 종료
gameover()
