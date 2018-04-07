import markovify
import os
import random
import nltk

sad_source = 'modest_mouse_lyrics_sad.txt'
happy_source = 'modest_mouse_happy.txt'
manic_source = 'modest_mouse_lyrics_manic.txt'


with open(sad_source, "r") as f:
    text1 = f.read()
with open(happy_source, "r") as f:
    text2 = f.read()
with open(manic_source, "r") as f:
    text3 = f.read()

text_model1 = markovify.Text(text1)
text_model2 = markovify.Text(text2)
text_model3 = markovify.Text(text3)

def welcome_screen():
    print("Welcome to the Modest Mouse Lyric Generator v1.0a!")
    user_input = input("We'll generate a Modest Mouse Song based on your mood. If you're feeling happy, sad, or manic, type it in!")
    return user_input
#def happy(str):
    #if user_input1 == 'Happy' or 'happy':
        #for i in range(15):
            #print(text_model1.make_sentence())

#def sad(str):
    #if user_input1 == 'Sad' or 'sad':
        #for i in range(15):
            #print(text_model2.make_sentence())

#def manic(str):
    #if user_input1 == 'Manic' or 'manic':
        #for i in range(15):
            #print(text_model3.make_sentence())

def main():
    while True:
        user_input = welcome_screen()
        if user_input == 'Happy' or 'happy':
            for i in range(15):
                print(text_model2.make_sentence.random.generate())
        if user_input == 'Sad' or 'sad':
            for i in range(15):
                print(text_model1.make_sentence.random.generate())
        if user_input == 'Manic' or 'manic':
            for i in range(15):
                print(text_model3.make_sentence.random.generate())
                break




main()
