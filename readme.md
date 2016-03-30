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

3) word list from  http://scrabblehelper.googlecode.com/svn-history/r20/trunk/ScrabbleHelper/src/dictionaries/sowpods.txt, renamed scrabble.txt

4) word list from  https://github.com/dwyl/english-words/blob/master/words.txt, renamed wordsFromGit.txt


5) nouns list from http://www.desiquintans.com/nounlist
                   http://www.desiquintans.com/downloads/nounlist/nounlist.txt.



### Python script
My script is (anagramSolver7.py) in this repository and it works as follows.
The purpose of this script is to find if not the conundrum the longest words possible.

The script will find all conundrums if any and all other words of decreasing length possible.

I have used lists, sets, in/not in and for else  statements to complete this task.
As a pyhton script i have opted to use one of the best built in tools **itertools**


This is an example showing how the list and set contents remain the same. This will only occur as long as the input
letters are unique. In this example 'abc'

```
Enter letters: abc
Perms: ['a', 'b', 'c', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba']
Len perms:  15
Set:  {'ca', 'bc', 'c', 'ba', 'b', 'cb', 'acb', 'cba', 'abc', 'bca', 'a', 'bac', 'ac', 'cab', 'ab'}
Len set:  15

```

Once the input has repeated input letters the set removes duplicates close to half the size of the list.


```

Enter letters: aba
Perms: ['a', 'b', 'a', 'ab', 'aa', 'ba', 'ba', 'aa', 'ab', 'aba', 'aab', 'baa', 'baa', 'aab', 'aba']
Len perms:  15
Set:  {'ba', 'ab', 'b', 'aba', 'aab', 'aa', 'baa', 'a'}
Len set:  8


```


### Preprocessing

I have not opted for preprocessing steps or techniques such as Pickle in this script.


## Efficiency

```
Random vowels:  ['i', 'a', 'i', 'e']
Random cons:  ['s', 'l', 's', 'd', 't']
All together now:  saitseldi
Parse file and split to list:  0.361319 seconds
Total List Contents:  267751
Total Set Contents:  155302
Parse file and create set_contents time:  0.41156699999999996 seconds
Total List Contents Nouns:  2334
Total Set Nouns:  2326
Before printing time:  0.567304 seconds

```

## Results

```
----------------------------
InputLetters: saitseldi
----------------------------
Total possible words: 407
----------------------------
Conundrums:  ['idealists']
----------------------------
Possible 8: ['dialists', 'idealist']
----------------------------
Possible 7: ['deasils', 'dialist', 'sialids', 'details', 'desalts', 'delists', 'distils', 'laities', 'dilates', 'saidest', 'liaises', 'dissea
t', 'silesia', 'dailies', 'daisies', 'salties', 'aidless', 'sedilia', 'liaised']
----------------------------

```
