#클래스
class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 

  def Sayhello(self,to_name):
   print("안녕" + to_name + "나는" + self.name)
 
  def introduce(self):
   print("내 이름은" +   self.name +" 그리고 나는" + str(self.age) + "살이야")


# 상속
class police(person):
  def arrest(self,to_arest):
    print("넌 체포됬다" + to_arest)

class programmer(person):
  def program(self,to_program):
    print("다음에 뭘 만들지? 아 이걸 만들어야 갰다" + to_program)

jenny = police("제니",25)
tony = programmer("토니", 23)
wonie = person("워니",20) # 오브젝트

wonie.introduce()
jenny.introduce() # police 클래스가 person 클래스를 상속 받았기 때문에 사용 가능
jenny.arrest("tony")
tony.program("인공지능")


