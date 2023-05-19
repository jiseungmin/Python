# 문자열
jumin = "900908-3232614"
print("생년= " + jumin[0:2])  # 0부터 2 직전까지 (0,1)
print("월= " + jumin[2:4])
print("일= " + jumin[4:6])
print("생년월일 = " + jumin[:6])
print("뒷자리 = " + jumin[7:])
print("숫자띄어쓰기 ="+jumin[:8:2])  # [:8:3] # 3은 인덱스 증가시켜서 출력함


# 문자열 처리함수
python = "python is amazing"
print(python.upper())  # 대문자로 변경
print(python.lower())  # 소문자롤 변경
print(python[0].isupper)  # 대문자 판단후 T/F 출력
print(len(python))
print(python.replace("python", "java"))
index = python.index("n")  # n이 어디 자리에 있는지
print(index)
print(python.find("python"))  # 값이 있을때 0 반환 없으면 -1 반환
print(python.count("n"))  # n이 몇개 있는지


# 문자열 포맷
print("나는 %d살 입니다." % 20)  # 방법1
print("나는 {}이고 {}살입니다.".format("철수", 13))  # 방법 2
print("나는 {name}이고 {age}살입니다.".format(name="철수", age=12))  # 방법 3
age = 20
name = "철수"
print(f"나는 {name}이고 {age}입니다.")  # 방법 4


# 탈출 문자
print("하이 \n안녕")
print("저는 \"지승민\" 입니다.")
print("Red Apple\rPine")  # \r 커서만큼 맨앞으로 이동
print("Redd\bApple")  # 앞에 한글자 지우기
print("Red\tApple")  # 탭
