import itertools
from itertools import permutations
import time



start_time = time.clock()

def getPerms():
    perms = []
    for perm in permutations(inputLetters):
        perms.append( "".join(perm))
    setPerms = set(perms)
    return setPerms

def getContents():
    # fr = open('scrabbleLower.txt', 'r')
    fr = open('uk.txt', 'r')
    content = fr.read()
    contents = content.split()
    setContents = set(contents)
    print('Total contents: ', len(contents))
    return setContents

def check(setPerms, setContents):
    results = []
    for word in setPerms:
        for w in setContents:
            if word not in setContents:
                break
        else:
            results.append(word.strip())
    print('Results: ', results)
    return results

def iterating(results, setContents):
    what = []
    for num in range(0,10):
        for w in results:
            test = itertools.combinations(w , num )
            for word in test:
                what.append(''.join(word))
                if len(word) <= 5:
                    if word in setContents:
                        print(str(word) + '\n')
    #print(what)
    #for p in what:


def iterating2(setContents, results):
    what = []

    for num in range(0,10):
        for w in results:
            test = itertools.combinations(w,num)
            for word in test:
                what.append(''.join(word))
    #for num in range(0,10):
    for f in what:
        if len(f) <= 9:
            if f in setContents:
                print(str(f))
    #print(what)


    #print(setPerms)




#getPerms()
#getContents()
#check(getPerms(), getContents())
inputLetters = input('Enter letters: ')

iterating(check(getPerms(), getContents()))
#iterating2(getContents(),check(getPerms(), getContents()))
