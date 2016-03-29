### Student name (Glen Gardiner)
#### Student number (G00305555)

# Countdown Letters Game Solver
Insert introduction here.
This gist is just an example of how you might layout your submission.
Please change it to suit your needs.

## Background
The first task I completed as part of this project was to Google "countdown letters game solver".
Google gave me two relevant results on the first page, these are [Cool Project name][2] and [Cool Solver][3].

## Words list
1) word list was created in class as wordlen9.txt
2) word list was created from unix command:  cat /usr/share/dict/words > words.txt
3) word list from  http://tug.ctan.org/tex-archive/syst...dt/dict/uk.zip i called uk.txt
4) word list from  http://scrabblehelper.googlecode.com/svn-history/r20/trunk/ScrabbleHelper/src/dictionaries/sowpods.txt
5) nouns list from http://www.desiquintans.com/nounlist
                   http://www.desiquintans.com/downloads/nounlist/nounlist.txt



## Python script
My script is in the files [anagramSolver.py](anagramSolver.py) in this repository and it works as follows.
The most important section is:

```python
import random
print(random.shuffle("My code is cool."))
```

Previously it looks like this:
```python
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.


## References
[1]: http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/
[2]: http://tug.ctan.org/tex-archive/syst...dt/dict/uk.zip
[3]: http://scrabblehelper.googlecode.com/svn-history/r20/trunk/ScrabbleHelper/src/dictionaries/sowpods.txt
[4]: https://github.com/dwyl/english-words/blob/master/words.txt
