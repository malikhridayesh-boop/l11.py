word = input("enter a word: ")
ch = input("enter a character: ")
for i in word:
    if (i == ch):
        print(ch,"is found")
        break
    else:
        print(ch,"is not found")