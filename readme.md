##Glen Gardiner -  G00305555

##Countdown Letters Game Solver


###Countdown Letters Game
Contestants are required to randomly select nine letters from two piles, vowels and consonants.
There has to be at least 3 vowels and at least 4 consonants in the complete selection.
Valid selections are (3 vowels and 6 cons, 4 vowels and 5 cons, 5 vowels and 4 cons)
In the game the players have 30 seconds to find the longest word possible using the selected letters.
Nouns are not permitted.
Points are .....



### Words list
I have used different collections of words found online and created from the system to test with.
The script will use any wordlist



1) word list was created from unix command:  cat /usr/share/dict/words > words.txt.

2) word list from  http://tug.ctan.org/tex-archive/syst...dt/dict/uk.zip i called uk.txt.

3) word list from  http://scrabblehelper.googlecode.com/svn-history/r20/trunk/ScrabbleHelper/src/dictionaries/sowpods.txt.

4) word list from  https://github.com/dwyl/english-words/blob/master/words.txt, renamed wordsFromGit.txt


5) nouns list from http://www.desiquintans.com/nounlist
                   http://www.desiquintans.com/downloads/nounlist/nounlist.txt.



### Python script
My script is (anagramSolver7.py) in this repository and it works as follows.
The purpose of this script is to find if not the conundrum the longest words possible.

The script will find all conundrums if any and all other words of decreasing length possible.

I have used lists, sets, in/not in and for else  statements to complete this task.
As a pyhton script i have opted to use one of the best built in tools **itertools**






### Preprocessing
I have not opted for preprocessing steps or techniques such as Pickle in this script.


## Efficiency

## Results


```
Random vowels:  ['o', 'i', 'e', 'a']
Random cons:  ['r', 'g', 'c', 's', 'd']
All together now:  oecidgrsa
Total List Contents:  354984
Total Set Contents:  354983
Parse file and create set_contents time:  0.498834 seconds
Total List Nouns:  2334
Total Set Nouns:  2326
Before printing time:  1.036014 seconds


```



```
----------------------------
InputLetters: oecidgrsa
----------------------------
Total possible words: 823
----------------------------
Conundrums:  []
----------------------------
Possible 8: ['radicose', 'disgrace', 'croisade', 'idocrase', 'cordages']
----------------------------
Possible 7: ['caserio', 'cadgers', 'cordies', 'scrogie', 'codgers', 'orgiacs', 'scoriae', 'agrised', 'socager', 'scaroid', 'codeias', 'dogear
s', 'cargoes', 'discage', 'soredia', 'cordage', 'croisad', 'sarcode', 'sarcoid', 'ardoise', 'radices', 'coraise', 'ergodic', 'corsage']
----------------------------

```
