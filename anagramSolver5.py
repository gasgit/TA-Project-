import itertools
from itertools import permutations

max_length = 9


def file_parser():
    fr = open('uk.txt','r')
    file_read = fr.read()
    file_content = file_read.split()
    fr.close()

    word_list = []
    for w in file_content:
        if w and len(w) <= max_length:
            word_list.append(w.lower())
    #print(word_list)
    print('Original fl: ', len(file_content))
    print('Length wl: ', len(word_list))
    return word_list

#file_parser()

def get_perms(input_letters):
    perms = []
    for perm in permutations(input_letters):
        perms.append( "".join(perm))
    print(perms)
    return perms




def user_input(input_letters):
    words_with_letters = []
    for word in file_parser():
        for letter in input_letters:
            if letter not in word:
                break
        else:
            #words_with_letters.append(word)
            if word and len(word) <= len(input_letters):
                words_with_letters.append(word)


    print(words_with_letters)
    print('words with letters: ', len(words_with_letters))
    return words_with_letters



input_letters = input('Enter letters: ')

#user_input(input_letters)

#permutations(input_letters)
get_perms(input_letters)
