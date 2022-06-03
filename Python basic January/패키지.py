# animal package
# dog, cat module
# dog, cat module can say "hi"
from animal import cat # 애니몰 패키지에 cat 모듈을 가지고 와줘
from animal import dog # 애니몰 패키지에 dog 모듈을 가지고 와줘
from animal import * # 애니몰 패키지에 있는 모든 모듈을 가지고 와줘

d = Dog()
c = Cat()

c.hi()
d.hi()

