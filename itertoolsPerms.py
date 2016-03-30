import itertools
from itertools import permutations



check_letters = input('Enter letters: ')


def check_tools():
    perms = []
    for i in range(1, len(check_letters) + 1):
        for p in permutations(check_letters, i):
            perms.append( "".join(p))
    print('Perms:' , perms)
    print('Len perms: ', len(perms))
    set_perms = set(perms)
    print('Set: ', set_perms)
    print('Len set: ', len(set_perms))

    return set_perms


check_tools()
