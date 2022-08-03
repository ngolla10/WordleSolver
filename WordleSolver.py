# Wordle Solver Version 4.0
# By: Dhita Srikanth and Nikhil Golla

# Welcome To Wordle Solver!
# This is an automation of the Wordle game that aims to reach a solution within 3 - 5 guesses
# Please ensure that your computer supports the listed Python packages before running the solver
# Disclaimer: Index Out of Bounds Error can occur if finalBank.txt has empty lines. Please them remove from the end.
# Up To Date List Of Used Words: https://www.stadafa.com/2021/09/every-worlde-word-so-far-updated-daily.html
# Content Inspiration: https://www.youtube.com/watch?v=YEoCBnQwdzM&ab_channel=AndrewSteele
# finalBank.txt Last Update: 8/2/22


import random
import webbrowser
import pyautogui
import time


# Variable Declarations, Opening and Reading Final Bank, Opening and Reading Used Words
wordlist = []
scraplist = []
end_game = False
guess = "crane"
daily_word = ""
my_file = open("finalBank.txt", "r")
data = my_file.read()
wordlist = data.split("\n")
oldlist = wordlist.copy()
my_file_two = open("usedWords.txt", "r")
data_two = my_file_two.read()
usedwordlist = data_two.split("\n")


# Remove Empty Strings
for word in wordlist:
    if word == "" or word == " ":
        wordlist.remove(word)


# Remove A Used Word From Word Bank
def delete(used_word):
    daily_word = used_word
    with open("finalBank.txt", "w") as file:
        for line in oldlist:
            if line != daily_word:
                file.write(line + "\n")

    with open("usedWords.txt", "w") as file_two:
        usedwordlist.insert(0, used_word)
        for line in usedwordlist:
            file_two.write(line + "\n")


# Detect Words With Repeated Letters
def double_word(word):
    letterlist = list(word)
    counter = 0
    origin = 0
    letter = 1
    for i in range(4):
        cutstring = letterlist[letter: 5]
        for i in range(len(cutstring)):
            if(letterlist[origin] == cutstring[i]):
                counter += 1
        letter += 1
        origin += 1
    if(counter > 0):
        return True
    else:
        return False


# Introduction
print("Hello, I am the Wordle Solver.")
time.sleep(1)
name = input("What Is Your Name?" + "\n")
print("Hello, " + name + ". Let's Get Started!")
time.sleep(1)
print("I Will Now Enter In The Starting Word: Crane")
time.sleep(1)


# Starting Word Entry
webbrowser.open("https://www.nytimes.com/games/wordle/index.html")
time.sleep(1.5)
pyautogui.typewrite("Crane", 0.15)
pyautogui.press('enter')


# Starting Word Result
print("What Was The Result Of The Guess?")
time.sleep(1)
results = input(
    "Enter Result As A String Of w, y, and g (w = white, y = yellow, g = green)" + "\n")

# Main Algorithm
for i in range(5):
    iteration = i
    if (results == "ggggg"):
        delete(guess)
        end_game = True
        break
    else:
        # Determine If Guess Has Double Letters
        if(double_word(guess) == True):
            for i in range(5):
                for word in wordlist:
                    if results[i] == 'w' and guess[i] == word[i] and word not in scraplist:
                        scraplist.append(word)
                    elif results[i] == 'y' and guess[i] == word[i] and word not in scraplist:
                        scraplist.append(word)
                    elif results[i] == 'y' and guess[i] not in word and word not in scraplist:
                        scraplist.append(word)
                    elif results[i] == 'g' and guess[i] != word[i] and word not in scraplist:
                        scraplist.append(word)
        else:
            for i in range(5):
                for word in wordlist:
                    if results[i] == 'w' and guess[i] in word and word not in scraplist:
                        scraplist.append(word)
                    elif results[i] == 'y' and guess[i] == word[i] and word not in scraplist:
                        scraplist.append(word)
                    elif results[i] == 'y' and guess[i] not in word and word not in scraplist:
                        scraplist.append(word)
                    elif results[i] == 'g' and guess[i] != word[i] and word not in scraplist:
                        scraplist.append(word)
        for word in scraplist:
            if(wordlist.__contains__(word)):
                wordlist.remove(word)
        print("Wordlist Count: " + str(len(wordlist)))
        with open("tester.txt", "w") as file:
            for line in wordlist:
                file.write(line + "\n")
        time.sleep(1)
        print("I will now pick a word at random. View all of your options in tester.txt")
        time.sleep(1)
        if(len(wordlist) > 0):
            new_guess = random.choice(wordlist)
        else:
            print("An error has occurred. Press 'n' to stop")
        decision = input("Try: " + new_guess + "? (Y/N)" + "\n")
        time.sleep(1)
        if(decision == "Y" or decision == "y"):
            guess = new_guess
            webbrowser.open("https://www.nytimes.com/games/wordle/index.html")
            time.sleep(1.5)
            pyautogui.typewrite(new_guess, 0.15)
            pyautogui.press('enter')
            scraplist.clear()
            results = input(
                "Enter Result As A String Of w, y, and g (w = white, y = yellow, g = green)" + "\n")
            if(results == "ggggg" and iteration == 4):
                delete(guess)
                end_game = True
        else:
            print("Thank you for playing!")
            break

if(end_game == False):
    print("You've reached the maximum amount of guesses. Better luck next time!")
else:
    print("Good Work! The Game Is Over")
