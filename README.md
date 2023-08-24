# Random Library Showcase
This repository is only a basic preview, consisting of a few minimal lines of code to give a brief understanding of the random library.
For a full overview of the Random module, please visit it's [official documentation](https://docs.python.org/3/library/random.html).
## Read the in-code comments for explainations on what each function and line does.


## Requirements
Random is a built-in library.
other libraries used such as time and os, are also built-in and simply require an import line. Such as:
### Import the random library
```
import random
```
This will also work with any other built-in library.

### Other modules used
```
import os, time
```

# File contents
All files in this repo relate to the random python library.

## main.py
[main](main.py) shows basic random functions, a small explaination and example outputs.

## guess_the_number.py
[guess the number](guess_the_number.py) showcases a basic guess the number game in which it will ask for a difficulty, changing the range of the random possible number from 1-10 all the way to 1-1000.
After it generates a random number, the user will get a chance to guess the generated number.
The file also contains input checks such as typechecks verifying the guess input is either "end" to end the game or a number. Any other input will not work.

## brute_force_attack.py
[brute force attack](brute_force_attack.py) shows and explains how to use the random library to brute force attack a password. 
Altough it is a simple brute force attack only using variables, it's theory is there and able to be easily transitioned to any situation you need.
Furthermore, my brute force attack code adds all attempted passwords to a text file. Although this is good if you want to watch it working, it can cause mass amounts of used storage with no realistic benefit. Merely running it for 5 seconds can cause hundreds of thousands of lines of text if you have a relatively good computer. You can remove lines 17 & 35 to prevent this.
We randomly select a character set, then randomly select a character in the character sets list we made. This may be more effort than you wish to put in, luckily there are work-arounds.
For letters, numbers and punctuation, you can use a library that gives you the list instead of manually creating the lists.
### Easily get & use an ascii letter list 
```
import string
all_letters = list(string.ascii_letters)
```
