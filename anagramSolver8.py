import itertools, random, time
from itertools import permutations

import timeit
#python3 -mtimit -s'import anagramSolver7' 'anagramSolver7.get_contents()'

max_length = 9


# get all permutation for inputletters and return set
def get_perms():
    perms = []
    for i in range(2, len(inputLetters) + 1):
        for p in permutations(inputLetters, i):
            perms.append( "".join(p))
    set_perms = set(perms)
    return set_perms


start_time = time.clock()

# get contents of processed file
def get_contents():
    with open('processedFile.txt', 'r') as f:
        con = []
        content = f.read()
        contents = content.split()
        for w in contents:
            con.append(w)
    set_contents = set(con)
    print('Total List Contents: ', len(contents))
    print('Total Set Contents: ', len(set_contents))
    print('Parse file and create set_contents time: ', time.clock() - start_time, "seconds")
    return set_contents
    return set_contents




# check set of unique words against inputletters and create new set set_contents_Checked
def set_content_input(set_contents):
    result = []
    for w in set_contents:
        for letter in w:
            if letter not in inputLetters:
                break
        else:
            result.append(w.strip())
    set_contents_Checked = set(result)
    return set_contents_Checked

# check set of perms against contents
# i loop this on to place results in place
def check(set_perms, set_contents_Checked):
    conundrums = []
    words8 = []
    words7 = []
    words6 = []
    words5 = []
    results = []
    for word in set_perms:
        for w in set_contents_Checked:
            if word not in set_contents_Checked:
                break
        else:
            results.append(word.strip())
            if(len(word) == max_length):
                conundrums.append(word)
                print('Conundrum found time: ' ,  time.clock() - start_time, "seconds")
            elif(len(word) == 8):
                words8.append(word)
            elif(len(word) == 7):
                words7.append(word)
            elif(len(word) == 6):
                words6.append(word)
            elif(len(word) == 5):
                words5.append(word)
            # elif(len(word) == 4):
            #     words4.append(word)
            # elif(len(word) == 3):
            #     words3.append(word)
            # else:
            #     print("Not Possible")

    print('Before printing time: ', time.clock() - start_time, "seconds")
    print_before = time.clock() - start_time

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
    print('Before printing time: ', print_before, "seconds")
    print('That time: ', time.clock() - start_time, "seconds")
    return results


def letters_selection():
    vowels = 'aaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiooooooooooooouuuuu'
    v = []
    consts = 'bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz'
    c = []

    for i in vowels:
        v.append(i)
    random.shuffle(v)

    for j in consts:
        c.append(j)
    random.shuffle(c)
    #
    # l = random.sample(v,3)
    # k = random.sample(c,6)

    #
    l = random.sample(v,4)
    k = random.sample(c,5)

    #
    # l = random.sample(v,5)
    # k = random.sample(c,4)


    # print('Random vowels: ', l)
    # print('Random cons: ', k)

    s = l+k
    random.shuffle(s)
    y = "".join(s)
    #print('All together now: ', y)
    return y


# for testing i like to use combinations i know manually
#inputLetters = input('Enter letters: ')


inputLetters = letters_selection()
#check(get_perms(), set_content_input(eliminate_nouns(get_contents(), get_nouns())))

check(get_perms(), set_content_input(get_contents()))


def timeTest():
    #check(get_perms(), set_content_input(get_contents()))
    #get_perms()
    #get_contents()
    #letters_selection()
    set_content_input(get_contents())


#timeTest()

#python3 -mtimeit -s'import anagramSolver8' 'anagramSolver8.timeTest()'
