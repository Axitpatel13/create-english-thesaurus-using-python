import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

#load the dict data
data = json.load(open('data.json'))

def eng_thesaurus(word):
    word = word.lower()
    
    #check for the exact word in the dict
    if word in data:
        found = data[word]
        for i in range(0, len(found)):
            if i == 0:
                print("Meaning:",found[i])
            else:
                print("Meaning: "+str(i+1)+ ":", found[i])
    #if word entered has incorrect spelliing
    else:
        #matches with the word with the closet spellinng
        closet_word = get_close_matches(word,data.keys(),cutoff=0.75)
        for j in range(0, len(closet_word)):
            print("Did you mean:",closet_word[j],"?")
            op = input("Press Y(Yes) | N(No) | E(Exit)")
            x = data[closet_word[j]]
            if op == "Y" or "y":
                for k in range(0,len(x)):
                    print("Meaning: ",str(i+1),":",x[k])
                break
            elif op == "N" or 'n':
                print("word does't exist")
                break
            elif op == "E" or "e":
                exit
                
print("\n Ctrl-c to exit")
while True:
    eng_thesaurus(input("Enter the word:"))