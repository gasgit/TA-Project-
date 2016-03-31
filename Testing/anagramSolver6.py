import itertools, random, time
from itertools import permutations


start_time = time.clock()
max_length = 9

# get all permutation in inputletters
def get_perms():
    perms = []
    for i in range(1, len(inputLetters) + 1):
        for p in permutations(inputLetters, i):
            perms.append( "".join(p))
    set_perms = set(perms)
    return set_perms


# parse file and create a set of unique words
def get_contents():
    #fr = open('scrabbleLower.txt', 'r')
    #fr = open('words.txt', 'r')
    fr = open('uk.txt', 'r')
    #fr = open('wordsFromGit.txt', 'r')
    con = []
    content = fr.read()
    contents = content.split()
    for w in contents:
        con.append(w)
    set_contents = set(con)
    print('Total List Contents: ', len(con))
    print('Total Set Contents: ', len(set_contents))
    return set_contents



# check set of unique words against inputletters and put into new set
def set_content_input(set_contents):
    result = []
    for w in set_contents:
        for letter in w:
            if letter not in inputLetters:
                break
        else:
            result.append(w.strip())
    set_contents_C = set(result)
    return set_contents_C

# check set of perms against contents
def check(set_perms, set_contents_C):
    conundrums = []
    words8 = []
    words7 = []
    words6 = []
    words5 = []
    results = []
    for word in set_perms:
        for w in set_contents_C:
            if word not in set_contents_C:
                break
        else:
            results.append(word.strip())
            if(len(word) == max_length):
                conundrums.append(word)
            elif(len(word) == 8):
                words8.append(word)
            elif(len(word) == 7):
                words7.append(word)
            elif(len(word) == 6):
                words6.append(word)
            elif(len(word) == 5):
                words5.append(word)
            # elif(len(word) == 4):
            #     words5.append(word)
            # elif(len(word) == 3):
            #     words5.append(word)
            # elif(len(word) == 2):
            #     words5.append(word)
            # elif(len(word) == 2):
            #     words5.append(word)
            # elif(len(word) == 1):
            #     words5.append(word)
            # else:
            #     print("Not Possible")

    print('That took: ', time.clock() - start_time, "seconds")

    print('Results: ', sorted(results, key=len))
    print('----------------------------')
    print('InputLetters:', inputLetters)
    print('----------------------------')
    print('Total possible words:', len(results))
    print('----------------------------')
    print('Conundrums: ', conundrums)
    print('----------------------------')
    print('Possible 8:', words8)
    print('----------------------------')
    print('Possible 7:', words7)
    print('----------------------------')
    print('Possible 6:', words6)
    print('----------------------------')
    print('Possible 5:', words5)
    print('----------------------------')

    print('That took: ', time.clock() - start_time, "seconds")
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
    print('All together now: ', y)
    return y


inputLetters = input('Enter letters: ')
def input_letters():
    inputLetters = selection(vowels(),cons())
    return inputLetters

#inputLetters = input_letters()
check(get_perms(), set_content_input(get_contents()))
