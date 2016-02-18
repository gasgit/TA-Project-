#!/usr/bin/python3

# get words text file from unix
# cat /usr/share/dict/words > words.txt


def createAnagramsArray():

    for words in contents:
        for letter in inputLetters:
            if letter not in words:
                break
        else:
            WordsContainingLetters.append(words.strip())
    print(WordsContainingLetters)
    print('Total Words in file: ', len(contents))
    print('WordsContainingLetters:', len(WordsContainingLetters))


def createResultsArray():
    result = []
    for w in WordsContainingLetters:
        for letter in w:
            if letter not in inputLetters:
                break
        else:
            result.append(w.strip())
    print('Actual Anagrams: ', result)





fr = open('uk.txt', 'r')
content = fr.read()
contents = content.split()


inputLetters = input('Enter letters: ')
WordsContainingLetters = []
createAnagramsArray()
createResultsArray()
