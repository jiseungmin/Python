subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "정형돈"]
print(subway)

print(subway.index("조세호"))  # 몇번째에 위치하고 있는가

subway.append("박명수")  # 리스트에 추가
print(subway)

subway.insert(1, "하하")  # 리스트 1번위치에 추가
print(subway)

subway.pop()  # 리스트 뒤에 부터 삭제
print(subway)

subway.append("유재석")
print(subway.count("유재석"))  # 유재석 갯수

mid = [1, 42, 3, 41, 2]
mid.sort()  # 정렬
print(mid)

mid.reverse()  # 거꾸로 정렬
print(mid)

mid.clear()  # 리스트 안 전체 삭제
print(mid)

mid.extend(subway)  # 배열 확장
print(mid)
