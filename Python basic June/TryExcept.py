try:
    print("나누기 계산기 입니다.")
    a = int(input("숫자를 입력해주세요."))
    b = int(input("숫자를 입력해주세요."))
    if a > 10 or b > 10:
        raise ValueError  # 에러 발생시키기
    print("값은 {}입니다.".format(a/b))
except ValueError:  # 벨류값이 에러일때
    print("잘못된 값을 입력했다")
except ZeroDivisionError as err:  # 0일때 값이 err
    print(err)
except Exception as err:  # 알수없는 err
    print("알수없는 에러가 생겼습니다.")
    print(err)
finally:  # 에러가 발생해도 실행
    print("계산기를 이용해줘서 고맙다.")
