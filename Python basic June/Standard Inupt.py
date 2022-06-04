# 표준 출력
print("python", "java", sep=",")  # sep = "," 출력값 빈공간을 ,로

score = {"수학": 0, "영어": 50, "과학": 20}
for subject, score in score.items():
    # ljust 우측정렬 후 오른쪽으로 빈공간 8개 생성, rjust 왼쪽정렬 후 왼쪽으로 빈공간 4개 생성
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기 순번표 001, 002 , 003
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))  # zfill(3) 000으로 채윰

# 출력 포맷

# 빈자리는 빈공간으로 두고 오른쪽으로 정렬하되 총 10칸 공간 확보
print("{:>10}".format(500))
# 빈자리는 빈공간으로 두고 왼쪽으로 정렬하되 총 10칸 공간 확보
print("{:<10}".format(500))
# 3칸씩 , 찍기
print("{:,}".format(100000000000))
# 오른쪽 정렬 하되 빈공간 ^으로 처리
print("{:^>10}".format(4000))
# 소수점 처리
print("{:f}".format(5/3))
# 소수점 2째 자리 처리
print("{:.2f}".format(5/3))
