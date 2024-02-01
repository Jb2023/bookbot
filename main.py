import re
def main():
    filePath = 'frakenstein.txt'
    text = book_text(filePath)
    letterTotal = letter_counter(text)
    dictionary = word_dictionary(text)

    print("Reading book...")
    print(f"Total number of words: {letterTotal}")
    for i in dictionary:
        if str(i) == "": 
            continue
        print("The char "+ str(i) + " was found " + str(dictionary[i]) + " times")
    print("End")

def book_text(path):
    with open(path) as f:
        return f.read().split()

    
def letter_counter(text):
    return len(text)


def word_dictionary(words):
    letters = {}
    rgx = re.compile("[^a-zA-Z]") 
    for i in words:
        for i in i:
            i = re.sub(r'[^a-zA-Z]', '',i)
            x = i.lower()
            if x in letters:
                letters[x]+=1
            else :
                letters[x] = 1
    return letters
    

main()