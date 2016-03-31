import itertools, random, time
from itertools import permutations

import timeit
#python3 -mtimit -s'import anagramSolver7' 'anagramSolver7.get_contents()'

max_length = 9


get_perms_time = time.clock()

# get all permutation for inputletters and return set
def get_perms():
    perms = []
    for i in range(2, len(inputLetters) + 1):
        for p in permutations(inputLetters, i):
            perms.append( "".join(p))
    print('Perms @', time.clock() - get_contents_time)
    set_perms = set(perms)
    print('Set perms @:', time.clock() - get_perms_time, "seconds")
    return set_perms


get_contents_time  = time.clock()

# get contents of processed file
def get_contents():
    with open('processedFile.txt', 'r') as f:
        con = []
        content = f.read()
        contents = content.split()
        for w in contents:
            con.append(w)
    set_contents = set(con)
    print('Total List Contents:', len(contents))
    print('Total Set Contents:', len(set_contents))
    print('Parse file @:', time.clock() - get_contents_time, "seconds")
    return set_contents



check_input = time.clock()

# check set of unique words against inputletters and create new set set_contents_Checked
def set_content_input(set_contents):
    result = []
    for w in set_contents:
        for letter in w:
            if letter not in inputLetters:
                break
        else:
            result.append(w)
    set_contents_Checked = set(result)
    return set_contents_Checked
    print('Check Input @:', time.clock() - check_input, "seconds")


checking_time = time.clock()
# check set of perms against contents
# i loop this on to place results in place
def check(set_perms, set_contents_Checked):
    words9 = []
    words8 = []
    words7 = []
    words6 = []
    words5 = []
    words4 = []
    words3 = []
    results = []
    for word in set_perms:
        for w in set_contents_Checked:
            if word not in set_contents_Checked:
                break
        else:
            results.append(word.strip())
            if(len(word) == max_length):
                words9.append(word)
                print('Found 9 @:' ,  time.clock() - checking_time, "seconds")
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
            else:
                pass

    print('Before print @:', time.clock() - checking_time, "seconds")
    print_before = time.clock() - checking_time

    print('Results: ', sorted(results, key=len))
    print('----------------------------')
    print('InputLetters:', inputLetters)
    print('----------------------------')
    print('Total possible words:', len(results))
    print('----------------------------')
    print('Possible 9:', words9)
    print('----------------------------')
    print('Possible 8:', words8)
    print('----------------------------')
    print('Possible 7:', words7)
    print('----------------------------')
    print('Possible 6:', words6)
    print('----------------------------')
    print('Possible 5:', words5)
    print('----------------------------')
    print('Before print @:', print_before, "seconds")
    print('Total @:', time.clock() - checking_time, "seconds")
    return results


inputLetters_time = time.clock()
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


    print('Random vowels:', l)
    print('Random cons:', k)

    s = l+k
    random.shuffle(s)
    y = "".join(s)
    print('InputLetters:', y)
    print('InputLetters @:', time.clock() - inputLetters_time, 'seconds')
    return y


############################  run from here  ###############################

# to enter letters manually
#inputLetters = input('Enter letters: ')

# to run random selection
inputLetters = letters_selection()


check(get_perms(), set_content_input(get_contents()))


#def timeTest():
    #check(get_perms(), set_content_input(get_contents()))
    #get_perms()
    #get_contents()
    #letters_selection()
    #set_content_input(get_contents())

#timeTest()

#python3 -mtimeit -s'import anagramSolver8' 'anagramSolver8.timeTest()'
