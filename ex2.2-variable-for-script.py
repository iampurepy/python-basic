######################################## HOW TO PASS A VARIABLE TO A SCRIPT###########################################
# ex 2.14 inside book
# input method you can use to pass variables to a script (script
# being another name for your .py ﬁles)
# Dung chuc nang Terminal cua Pycharm.
# Notes: type command correct, never forget variables , ex:>python test.py apple orange grapefruit,apple orange grapefruid are variables

from sys import argv
script, user_name = argv
prompt = '>'
print(f"Hi {user_name}, I am the {script}")
print("Please answer some questions. Do you like me?")
likes = input()
print(f"Where live, {user_name} ?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print(f"Ok. You have said you like {likes} and "
      f"live in {lives}. "
      f"You are using {computer}.")



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
"""
1.difference between argv and input()? The difference has to do with where the user
is required to give input. If they give your script inputs on the command line, then you use argv.
If you want them to input using the keyboard while the script is running, then use input().
"""
