# 일반 유닛
class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛이동]")
        print("{}이 {}로 이동합니다. 속도:[{}]".format(self.name, location, self.speed))

# 공격 유닛


class attackunit(unit):  # 부모클래스 unit에 자식클래스 attackunit이 상속 받음
    def __init__(self, name, hp, damage, speed):
        unit.__init__(self, name, hp, speed)  # unit에 __init__메소드를 상속받음
        self.damage = damage

    def attack(self, location):  # 클래스안에 메소드는 self를 꼭 넣어야함
        print("{}이 {}방향으로 공격하였습니다.".format(self.name, location))

    def damaged(self, damage):
        print("{}이 {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{}이 죽었습니다.".format(self.name))
        else:
            print("{}이 {}체력이 남았습니다.".format(self.name, self.hp))


firebat = attackunit("파이어뱃", 50, 50, 5)
firebat.attack("5시")
firebat.damaged(25)
firebat.damaged(25)

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


vulture = attackunit("벌쳐", 100, 20, 30)
vulture.move("9시")

battle = flyingAttackunit("배틀크루저", 50, 300, 10)
battle.attack("9시")
battle.move("9시")
