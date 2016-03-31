import itertools
from itertools import permutations


max_length = 9


inputLetters = input('Enter letters: ')


def get_perms(inputLetters):
    perms = []
    for i in range(1, len(inputLetters) + 1):
        for p in permutations(inputLetters, i):
            v = hash( "".join(p))
            perms.append( ("".join(p), v) )
    print('Perms:' , perms)
    print('Len perms: ', len(perms))
    set_perms = set(perms)
    print('Set: ', set_perms)
    print('Len set: ', len(set_perms))
    print(type(set_perms))
    for x in set_perms:
        if 'a' == x[0]:
            print(x[1])
    return set_perms


def check_set_perms(inputLetters, set_perms):
    h = hash(inputLetters)
    for i in set_perms:
        if h == i[1]:
            print(i)






def get_contents():
    with open('processedFile.txt', 'r') as f:
        con = []
        content = f.read()
        contents = content.split()
        for w in contents:
            v = hash(w)
            con.append((v,w))
    set_contents = set(con)
    print('Total List Contents: ', len(contents))
    print('Total Set Contents: ', len(set_contents))
    # print('Parse file and create set_contents time: ', time.clock() - start_time, "seconds")
    #print(set_contents)

    return set_contents

def check_content_input(set_contents):
    result = []
    h = hash(inputLetters)
    for x in set_contents:
        if x[0] == h:

            print(h,x[1])
            result.append(h)

    set_contents_Checked = set(result)
    print(set_contents_Checked)
    return set_contents_Checked


check_content_input(get_contents())


#get_contents()
#get_perms(check_letters)
#check_set_perms(check_letters, get_perms(check_letters))
