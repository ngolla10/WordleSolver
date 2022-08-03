# with open('words.txt') as new_file:

#     line_one = new_file.readline()
#     final_line = line_one[0:5]
#     final_line = final_line.lower()

# print(line_one)
# print(final_line)


# with open('words.txt') as new_file:

#     for i in range(396):
#         line_one = new_file.readline()
#         final_line = line_one[0:5]
#         final_line = final_line.lower()
#         newer_file = open("words2.txt", "a")
#         newer_file.write(final_line + "\n")

# array_one = ["trae", "molly", "jordan", "kyle"]
# array_two = ["trae", "vanessa", "jordan", "derek"]

# for i in range(len(array_two)):
#     if(array_one.__contains__(array_two[i])):
#         array_one.remove(array_two[i])
# print(array_one)


# with open("wordBank.txt", "r") as fp:
#     lines = fp.readlines()


# with open("wordBank.txt", "w") as fp:
#     with open("usedWords.txt") as pp:
#         for i in range(397):
#             line_one = pp.readline()
#             for line in lines:
#                 if line.strip("\n") != line_one:
#                     fp.write(line)

# with open("wordBank.txt", "r") as fp:
#     lines = fp.readlines()

# with open("usedWords.txt", "r") as pp:
#     words = pp.readlines()

# with open("wordBank.txt", "w") as fp:
#     # for line in lines:
#     #     if line.strip("\n") != "angry":
#     #         fp.write(line)
#     for word in words:
#         for line in lines:
#             if line.strip("\n") != word.strip("\n"):
#                 fp.write(line)


# version 1:
# with open("wordBank.txt", "r") as fp:
#     lines = fp.readlines()

# with open("wordBank.txt", "w") as fp:
#     for line in lines:
#         if line.strip("\n") != "hello":
#             fp.write(line)


# with open("wordBank.txt", "r") as fp:
#     lines = fp.readlines()

# with open("usedWords.txt", "r") as pp:
#     words = pp.readlines()

# if lines.__contains__(words[3]):
#     lines.remove(words[3])
#     print(lines[4504:4509])


# correct:
# with open("wordBank.txt", "r") as fp:
#     lines = fp.readlines()  # gets stored as an array


# with open("usedWords.txt", "r") as pp:
#     words = pp.readlines()  # gets stored as an array

# for i in range(396):
#     if(lines.__contains__(words[i])):
#         lines.remove(words[i])

# for line in lines:
#     newer_file = open("beta.txt", "a")
#     newer_file.write(line)

# with open("beta.txt", "r") as fp:
#     lines = fp.readlines()  # gets stored as an array

# with open("usedWords.txt", "r") as pp:
#     words = pp.readlines()  # gets stored as an array

# counter = 0
# for word in words:
#     if(lines.__contains__(word)):
#         counter += 1

# print(counter)

# with open("finalBank.txt", "r") as fp:
#     lines = fp.readlines()  # gets stored as an array
#     lines.sort()

# for line in lines:
#     newer_file = open("finalBank2.txt", "a")
#     newer_file.write(line)

# results = "ggggg"
# print(results[3])


# important:
# with open("finalBank.txt", "r") as fp:
#     lines = fp.readlines()

# for line in lines:
#     if(line[0] == "t" and line[1] == "r" and line[4] == "e"):
#         newer_file = open("tester.txt", "a")
#         newer_file.write(line)

# grade = 50

# if(grade == 50):
#     print("yes")
# elif(grade < 60):
#     print("true")
# elif(grade < 70):
#     print("True")


# Original Algorithm:

# Get list of all allowed words from txt file into a list
# comment:
# guess = ""
# results = ""
# remaining_guesses = 5
# guesslist = []

# for guesses in range(5):
#     guess = input("Input guess:")
#     if guess in wordlist:
#         guesslist.append(guess)
#         remaining_guesses = remaining_guesses - (len(guesslist)-1)
#         if results == "ggggg":
#             print("good work")
#             break
#         reflist = list(wordlist)
#         for word in reflist:
#             for i in range(5):
#                 if results[i] == 'w' and guess[i] in word:
#                     wordlist.remove(word)
#                     break
#                 elif results[i] == 'y' and guess[i] == word[i]:
#                     wordlist.remove(word)
#                     break
#                 elif results[i] == "y" and guess[i] not in word:
#                     wordlist.remove(word)
#                     break
#                 elif results[i] == 'g' and guess[i] != word[i]:
#                     wordlist.remove(word)
#                     break

#         print("Try:"+random.choice(wordlist))
#     else:
#         print("Enter valid word")

# listone = [1, 2, 3, 4]
# listtwo = [1, 2, 3, 4, 5, 6, 7]
# for number in listone:
#     if(listtwo.__contains__(number)):
#         listtwo.remove(number)
# print(listtwo)

# stringa = "yellow"
# stringb = "YELLOW"
# print(stringa == stringb)

# listone = [1, 2]

# for i in range(len(listone)):
#     if (listone[100] == 5):
#         print("hello")
# word = "niagrafalls"
# print(word[2])
# listone.remove(listone[len(listone) - 1])
# print(listone)

# for i in range(5):
#             for word in wordlist:
#                 if results[i] == 'w' and guess[i] in word:
#                     wordlist.remove(word)
#                 elif results[i] == 'y' and guess[i] == word[i]:
#                     wordlist.remove(word)
#                 elif results[i] == "y" and guess[i] not in word:
#                     wordlist.remove(word)
#                 elif results[i] == 'g' and guess[i] != word[i]:
#                     wordlist.remove(word)
# listOne = [1, 2, 3, 4, 5, 1]
# listOne.remove(1)
# print(listOne)

# def double_word(word):
#     letterlist = list(word)
#     counter = 0
#     origin = 0
#     letter = 1
#     for i in range(4):
#         cutstring = letterlist[letter: 5]
#         for i in range(len(cutstring)):
#             if(letterlist[origin] == cutstring[i]):
#                 counter += 1
#         letter += 1
#         origin += 1
#     if(counter > 0):
#         print(True)
#     else:
#         print(False)
# clean final bank again:
# with open("wordBank.txt", "r") as fp:
#     lines = fp.readlines()  # gets stored as an array


# with open("usedWords.txt", "r") as pp:
#     words = pp.readlines()  # gets stored as an array

# for i in range(len(words)):
#     if(lines.__contains__(words[i])):
#         lines.remove(words[i])

# with open("finalBank.txt", "w") as file:
#     for line in lines:
#         file.write(line)
