from hangmancls import HangmanGame
print("===========HANG-MAN===========")
wordlist = [
            "MAN",
            "GANG",
            "HANG",
            "APPLE",
            "BANANA",
            "DOG",
            "CAT",
            "BIRD",
            "BOOK",
            "DESK",
            "PARK",
            "SUN",
            "MOON",
            "HELLO",
            "LENGTH",
            "WORLD",
        ]
game = HangmanGame(wordlist)
print(game.word)
print(" ".join(game.answer), f"({game.word_length}글자)")
game.play()