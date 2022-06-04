# 딕셔너리

cabinet = {3: "강호동", "a-30": "유재석"}  # dictionary 선언
print(cabinet[3], cabinet["a-30"])

cabinet["a-30"] = "박명수"  # dictiolnary 초기화
print(cabinet["a-30"])

del cabinet["a-30"]  # dictionary 제거
print(cabinet)

cabinet[23] = "유재석"
print(cabinet.keys())  # key 값만
print(cabinet.values())  # Value 값만
print(cabinet.items())  # item


cabinet.clear()


# 튜플 ->  변경 불가능 리스트
x = (1, 2, 3)
y = ("a", "b", "c")
