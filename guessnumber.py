import random
limit = 100

def guess_number():
    number = random.randint(1, limit)
    print(f"숫자를 맞춰보세요! (1-{limit})")

    for i in range(1,8):
        try:
            guess = int(input("숫자를 입력하세요: "))

            if guess < number:
                print("더 큰 숫자입니다.")
                
            elif guess > number:
                print("더 작은 숫자입니다.")
            else:
                print("축하합니다! " + str(i) + "번 만에 숫자를 맞췄습니다!")
                break
            if i == 7:
                print("(Computer-Win)아쉽지만, 정답은 " + str(number) + "였습니다.")
                break
        except ValueError:
            print("유효한 숫자를 입력해주세요.")

guess_number()