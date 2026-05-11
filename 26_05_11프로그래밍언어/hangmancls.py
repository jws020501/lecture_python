import random

class HangmanGame:
    MASK_CHAR = "_"
    def __init__(self,wordlist):
        self.word_list = wordlist
        self.word = random.choice(self.word_list).upper()
        self.word_length = len(self.word)
        self.answer = [HangmanGame.MASK_CHAR] * self.word_length
        self.max_attempts = self.word_length + 9
        self.used_letters = set()

    def reveal_letter(self, letter):
        for idx, ch in enumerate(self.word):
            if ch == letter:
                self.answer[idx] = letter

    def play(self):

        for turn in range(1, self.max_attempts + 1):
            user_input = input("알파벳 입력: ").strip().upper()

            if len(user_input) != 1 or not user_input.isalpha():
                print("알파벳 1글자만 입력하세요")
                continue

            if user_input in self.used_letters:
                print(f"{user_input}은 이미 입력하셨습니다")
                continue

            self.used_letters.add(user_input)

            if user_input in self.word:
                self.reveal_letter(user_input)
                print(f"맞음 {self.max_attempts - turn}번 남았습니다")
            else:
                print(f"틀림 {self.max_attempts - turn}번 남았습니다")

            print(" ".join(self.answer))

            if "_" not in self.answer:
                print("이겼습니다")
                return

        print("해결하지 못했습니다")
