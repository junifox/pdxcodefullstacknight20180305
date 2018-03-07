import random
question = input("Do you want a random emoticon?")
emoticons = [">:[", "¯\_(ツ)_/¯", "(╬ Ò ‸ Ó)", "‎(ﾉಥ益ಥ）ﾉ ┻━┻", "( ͡° ͜ʖ ͡°)", "~ヾ(＾∇＾)"]
if question == "yes":
    print(random.choice(emoticons))
else:
    print("Then leave")
