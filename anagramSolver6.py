import itertools, random, time


from itertools import permutations

start_time = time.clock()
max_length = 9


## get all permutation in inputletters
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
    con = []
    fr = open('uk.txt', 'r')
    content = fr.read()
    contents = content.split()
    for w in contents:
        con.append(w)
    set_contents = set(con)
    print('Total contents: ', len(set_contents))
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
    #print('SET CONTENTS: ', sorted(setContentsC, key=len))
    return set_contents_C
    #print('Actual Anagrams: ', sorted(result, key=len))

# check set of perms against contents
def check(set_perms, set_contents_C):
    conundrums = []
    results = []
    for word in set_perms:
        for w in set_contents_C:
            if word not in set_contents_C:
                break
        else:
            results.append(word.strip())
            if(len(word) == max_length):
                conundrums.append(word)
    print('Results: ', sorted(results, key=len))
    print('Total possible words: ', len(results))

    print('inputLetters: ',inputLetters)
    print('Conundrums: ', conundrums)
    print('That took: ', time.clock() - start_time, "seconds")
    return sorted(results)

def vowels():
    vowels = 'aaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiooooooooooooouuuuu'
    v = []
    for i in vowels:
        v.append(i)
    random.shuffle(v)
    l = random.sample(v,4)
    print('Random vowels: ', l)
    return l

def cons():
    consts = 'bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz'
    c = []
    for j in consts:
        c.append(j)
    random.shuffle(c)
    k = random.sample(c,5)
    print('Random cons: ', k)
    return k

def selection(l,k):
    s = l+k
    random.shuffle(s)
    y = "".join(s)
    print('All together now: ', y)
    return y


#inputLetters = input('Enter letters: ')

inputLetters = selection(vowels(),cons())


check(get_perms(), set_content_input(get_contents()))
