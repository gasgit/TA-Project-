import random


vowels = 'aaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiooooooooooooouuuuu'
consts = 'bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz'

#vowels = 'aeiou'
#consts = 'bcdfghjklmnpqrstvwxyz'

v = []
for i in vowels:
    v.append(i)

print(v)
random.shuffle(v)

l = random.sample(v,5)
print(l)

c = []
for j in consts:
    c.append(j)
print(c)

random.shuffle(c)

k = random.sample(c,4)
print(k)



s = l+k
random.shuffle(s)
print(s)


y = "".join(s)

print(y)
