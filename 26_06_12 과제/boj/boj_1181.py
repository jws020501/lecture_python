# 1181번 (단어 정렬)
def word_sort():
    word_list = []
    input_word_num = int(input(f'입력할 단어의 수 : '))
    for _ in range(input_word_num):
        word = input(f'단어를 입력하시오 : ').lower()
        word_list.append(word)
    word_list = list(set(word_list))
    word_list.sort(key=lambda w: (len(w), w))

    for word in word_list:
        print(word)

word_sort()