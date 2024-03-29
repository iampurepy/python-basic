######################################## HOW TO PASS A VARIABLE TO A SCRIPT###########################################
# input method you can use to pass variables to a script (script
# being another name for your .py ﬁles)
# Dung chuc nang Terminal cua Pycharm.
# Notes: type command correct, never forget variables , ex:>python test.py apple orange grapefruit,apple orange grapefruid are variables
from sys import argv
print(argv)
khong,mot,hai,ba =  argv
print("The script is called:", khong )
print("Your first variable is:", mot)
print("Your second variable is:", hai)
print("Your third variable is:", ba)
""" 
Explain meaning:
On line 1 we have what’s called an import. This is how you add features to your script from the Python
feature set. Rather than give you all the features at once, Python asks you to say what you plan to use.
This keeps your programs small, but it also acts as documentation for other programmers who read your
code later.

The argv is the argument variable, a very standard name in programming that you will ﬁnd used in
many other languages. This variable holds the arguments you pass to your Python script when you run
it. In the exercises you will get to play with this more and see what happens.

Line 3 unpacks argv so that, rather than holding all the arguments, it gets assigned to four variables you
can work with: script, first, second, and third. This may look strange, but “unpack” is probably
the best word to describe what it does. It just says, “Take whatever is in argv, unpack it, and assign it
to all of these variables on the left in order.”
"""
