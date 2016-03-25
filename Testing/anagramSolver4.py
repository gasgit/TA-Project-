import itertools
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
    #print(perms)
    #print('Total perms: ', len(perms))
    return setPerms

getPerms()




def parse():
    fr = open('uk.txt', 'r')
    content = fr.read()
    contents = content.split()
    setContents = set(contents)
    #print(setContents)
    #print('Total contents: ', len(contents))

    r = []

    for h in setContents:
        for y in setPerms():
            if y not in h:
                break
            else:
                r. append(y)
                print(y)
    return r
parse()

print(r)

    # for word in setPerms:
    #     for w in setContents:
    #         if word not in setContents:
    #             break
    #     else:
    #         results.append(word.strip())
    #         #print(results)







print(time.clock() - start_time, "seconds")


# def it():
#     for s in r:
#         print(s)
#
# it()



#print(perms)
#print('Perms: ',len(perms))

# what = []
#
# newArray = []
#
# def iterating():
#
#     for num in range(0,10):
#         for run in results:
#             test = itertools.combinations(run , num )
#             for word in test:
#                 what.append(''.join(word))
#
#             setWhat=set(what)
#             print(setWhat)
#             #print("run ",run,len(what))
#             fr = open('words.txt', 'r')
#             content = fr.read()
#             contents = content.split()
#             setContents = set(contents)
#             #print('Total contents: ', len(contents))
#
#             for word in setContents:
#                 for w in setWhat:
#                     if word not in setWhat:
#                         break
#                 else:
#                     newArray.append(word.strip())
#                     fw.write(word + '\n')
#         newSet = set(newArray)
#     print(sorted(newSet))
#
# fw = open('itertools.txt','w' )
#
# iterating()
