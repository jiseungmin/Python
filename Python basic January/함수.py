
def chat(name1, name2, age):
    print("%5: 안녕? 넌 몇살이니?")
    print("%5: 나? 나는 %d" % (name1, age))

    chat("엘리스", "율하", 10)
    chat("철수", "영희", 30)


def dsum(a, b):
    result = a + b
    return result


d = dsum(2, 4)

print(d)
print("test")
