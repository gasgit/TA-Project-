max_length = 9

def processFile(file_name):
    fw = open('processedFile.txt', 'w')
    with open(file_name , 'r') as f:
        content = f.read()
        contents = content.split()
        for w in contents:
            if len(w) >2 and len(w) <= max_length and w.islower():
                fw.write(w + '\n')
    print('File Processed')
    print('Run:  python3 anagramSolver8.py')


#**************    choose one    **********************************

#file_name = 'british-english-insane.txt'
#file_name = 'words.txt'
#file_name = 'uk.txt'
file_name = 'wordsFromGit.txt'


processFile(file_name)
