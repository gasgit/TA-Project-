from itertools import permutations
import time

inputLetters = input('Enter letters: ')

perms = []
results = []

start_time = time.clock()

def getPerms():
    for perm in permutations(inputLetters):
        perms.append( "".join(perm))
    setPerms = set(perms)
    print(perms)

    fr = open('uk.txt', 'r')
    content = fr.read()
    contents = content.split()
    setContents = set(contents)
    print('Total contents: ', len(contents))

    for word in setPerms:
        for w in setContents:
            if word not in setContents:
                break
        else:
            results.append(word.strip())
            print(results)

getPerms()

print('Perms: ',len(perms))

print(time.clock() - start_time, "seconds")
