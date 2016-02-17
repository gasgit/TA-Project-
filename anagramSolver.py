#!/usr/bin/python3

# get words text file from unix
# cat /usr/share/dict/words > words.txt


def createAnagramsArray():
	w=0
	for words in fr:
		w+=1
		for letter in inputLetters:
			if letter not in words:
				break
		else:
			wordsContaingLetters.append(words.strip())
	print(wordsContaingLetters)
	print('Total Words in file: ', w)
	print('WordsContaingLetters:',len(wordsContaingLetters))


def createResultsArray():
	result = []
	for w in wordsContaingLetters:
	    for letter in w:
	        if letter not in inputLetters:
	            break
	    else:
	        result.append(w.strip())
	print('Actual Anagrams: ', result)


fr = open('words.txt','r')
inputLetters = input('Enter letters: ')
wordsContaingLetters = []
createAnagramsArray()
createResultsArray()
