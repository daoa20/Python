#import the definitions
import json
import difflib

from difflib import get_close_matches

#attribute the definitions to the data variable for it's use
data = json.load(open("data.json", "r"))

#function for keep knowing
def sure():
    may = input("Want to know anything else? (Y/N): ")
    if may.upper() == "Y":
        what()
    else:
        print("Goodye!")

#function for the user promtp
def what():
    word = input("What do you want to know? ")
    word = word.lower()
    #checks if the word exists and also return the definition
    if word in data:
        meaning = data[word]
        for i in meaning:
            print("* " + i)
    else:
        rw = get_close_matches(word, data.keys())
        if len(rw) > 0:
            rw = get_close_matches(word, data.keys())[0]
            right = input("Did you mean " + rw + "? (Y/N):")
            if right.upper() == 'Y':
                meanings = data[rw]
                for i in meanings:
                    print("* " + i)
            elif right.upper() == 'N':
                print("The word does not exist :(")
            else:
                print("I didn'y understand :(")
        else:
            print("The word does not exist :(")
    sure()

what()
