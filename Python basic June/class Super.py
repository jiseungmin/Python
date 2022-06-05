class unit:
    def __init__(self, speed):
        self.speed = speed
        print("unit 생성자")


class fltable:
    def __init__(self):
        print("unit 공중생성자")


class flyunit(fltable, unit):
    def __init__(self):
        super().__init__()  # 슈퍼는 상속받은 앞자리 fltable만 쓸수있음.


class groundunit(unit):
    def __init__(self, speed):
        super().__init__(speed)  # 슈퍼 상속받은 메소드 가져오기


dropship = flyunit()
people = groundunit(10)
