fr = open('scrabble.txt', 'r')
contents = fr.read()
content = contents.split()
#print(content)

fw = open('sacrabbleLower.txt', 'w')

for word in content:
    #print(word)
    fw.write(word.lower() + '\n')
