import pickle
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
socre_file = open("score.txt", "r", encoding="utf8")
print(socre_file.read())
socre_file.close()

socre_file = open("score.txt", "r", encoding="utf8")  # 한줄씩 출력
print(socre_file.readline(), end="")
print(socre_file.readline(), end="")
print(socre_file.readline(), end="")
print(socre_file.readline())
socre_file.close()

# pickle
profile_file = open("profile_pickle", "wb")
profile = {"이름": "박명수", "나이": 50, "취미": ["코딩", "낮잠"]}
print(profile)
pickle.dump(profile, profile_file)  # profile 에 있는 내용을 file에 저장
profile_file.close()

profile_file = open("profile_pickle", "rb")
profiles = pickle.load(profile_file)
print(profile)
profile_file.close()

# with
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부를 하고있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
