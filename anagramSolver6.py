import itertools, random, time
from itertools import permutations

#start_time = time.clock()

def getPerms():
    perms = []
    for i in range(1, len(inputLetters)):
        for p in permutations(inputLetters, i):
           perms.append( "".join(p))
    setWords = sorted(set(perms))
    return setWords

def getContents():
    #fr = open('scrabbleLower.txt', 'r')
    fr = open('uk.txt', 'r')
    content = fr.read()
    contents = content.split()
    setContents = set(contents)
    print('Total contents: ', len(contents))
    return setContents

def check(setWords, setContents):
    results = []
    for word in setWords:
        for w in setContents:
            if word not in setContents:
                break
        else:
            results.append(word.strip())
    print('inputLetters: ',inputLetters)
    print('Results: ', results)
    return results


def vowels():
    vowels = 'aaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiooooooooooooouuuuu'
    v = []
    for i in vowels:
        v.append(i)
    random.shuffle(v)
    l = random.sample(v,3)
    print('Random vowels: ', l)
    return l

def cons():
    consts = 'bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz'
    c = []
    for j in consts:
        c.append(j)
    random.shuffle(c)
    k = random.sample(c,6)
    print('Random cons: ', k)
    return k

def selection(l,k):
    s = l+k
    random.shuffle(s)
    y = "".join(s)
    print(y)
    return y



inputLetters = selection(vowels(),cons())

check(getPerms(), getContents())
