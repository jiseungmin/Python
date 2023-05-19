import os  # 운영체제에서 제공하는 기본 기능
import glob  # 경로 내의 폴더 / 파일 목록 조회
import time  # 시간 관련함수
import datetime  # 날짜 관련함수

print(glob.glob("*.txt"))
print(os.getcwd())
print(time.localtime())
print(datetime.date.today())
