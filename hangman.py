import random

word_list = ["MAN", "GANG", "HANG", "APPLE", "BANANA", "DOG", "CAT", "BIRD", "BOOK", "DESK", "PARK", "SUN", "MOON","HELLO","LENGTH","WORLD"]

rand_index = random.randint(0, len(word_list) - 1)
word = word_list[rand_index].upper()

ans = ["_"] * len(word)

print("===========HANG-MAN===========")

print(word) #이거는 테스트

print(" ".join(ans), "(" + str(len(word)) + "글자)")

for i in range(1,len(word) + 5):
    user_input = input("알파벳 입력: ").upper()

    if user_input in word and  len(user_input) == 1:
        if user_input in ans:
            print(str(user_input)+"은 이미 입력하셨습니다")
            continue
        for j in range(len(word)):
            if word[j] == user_input:
                ans[j] = user_input

        print("맞음 "+str(len(word) + 9 - i)+"번 남았습니다")
    else:
        print("틀림 "+str(len(word) + 9 - i)+"번 남았습니다")

    print(" ".join(ans))

    if "_" not in ans:
        print("이겼습니다")
        break
    if i==len(word) + 9:
        print("해결하지 못했습니다")
