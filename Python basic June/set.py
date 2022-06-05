# set 집합
# 중복 안됨, 순서 없음

my_set = {1, 2, 3, 4, 5}
print(my_set)

java = {"유재석", "박명수", "정형돈"}
python = set(["유재석", "하하", "양세형"])

print(java & python)  # 교집합
print(java | python)  # 합집합
java.add("하하")  # 추가
print(java)
python.remove("하하")  # 삭제
print(python)
