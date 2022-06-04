# 파일 입출력

# 파일 입력
socre_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=socre_file)
print("영어: 50", file=socre_file)
socre_file.close()

socre_file = open("score.txt", "a", encoding="utf8")
socre_file.write("과학: 80")
socre_file.write("\n정보 : 100")
socre_file.close()

# 파일 출력
socre_file = open("socre_file.txt", "r", encoding="utf8")
print(socre_file.read())
socre_file.close()
