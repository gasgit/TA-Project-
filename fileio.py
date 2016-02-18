from itertools import permutations


inputLetters = input('Enter letters: ')


perms = []
results = []

def getPerms():
    for perm in permutations(inputLetters):
        perms.append( "".join(perm))
    print(len(perms))
    #print(perms)

    setPerms = set(perms)
    #print(setPerms)

    fr = open('uk.txt', 'r')
    content = fr.read()
    contents = content.split()
    setContents = set(contents)

    for word in setPerms:
        for w in setContents:
            if word not in setContents:
                break

        else:
            results.append(word.strip())

            print('Perms: ',len(perms))
            print(results)


getPerms()










#
#
#
# print(contents)
