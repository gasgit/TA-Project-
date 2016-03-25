import random



#vowels = 'aeiou'
#consts = 'bcdfghjklmnpqrstvwxyz





def vowels():
    vowels = 'aaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiooooooooooooouuuuu'
    v = []
    for i in vowels:
        v.append(i)
    random.shuffle(v)
    l = random.sample(v,3)
    print(l)
    return l
#
#
#
def cons():
    consts = 'bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz'

    c = []
    for j in consts:
        c.append(j)
    random.shuffle(c)
    k = random.sample(c,6)
    print(k)
    return k
#
#
def selection(l,k):
    s = l+k
    random.shuffle(s)
    y = "".join(s)
    print(y)
    return y
#
#
# vowels()
#
# cons()
selection(vowels(),cons())
