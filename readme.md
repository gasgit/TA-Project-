##Glen Gardiner -  G00305555

##Countdown Letters Game Solver


###Countdown Letters Game
Contestants are required to randomly select nine letters from two piles, vowels and consonants.
There has to be at least 3 vowels and at least 4 consonants in the complete selection.
In the game the players have 30 seconds to find the longest word possible using the selected letters.
Nouns are not permitted.
Points are .....


For the purpose of this program is to find if not the conundrum the longest words possible.



### Words list
I have used different collections of words found online and created from the system to test with.
The script will use any wordlist.

1) word list was created from unix command:  cat /usr/share/dict/words > words.txt.

2) word list from  http://tug.ctan.org/tex-archive/syst...dt/dict/uk.zip i called uk.txt.

3) word list from  http://scrabblehelper.googlecode.com/svn-history/r20/trunk/ScrabbleHelper/src/dictionaries/sowpods.txt.

4) nouns list from http://www.desiquintans.com/nounlist
                   http://www.desiquintans.com/downloads/nounlist/nounlist.txt.



### Python script
My script is (anagramSolver.py) in this repository and it works as follows.




### Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.
