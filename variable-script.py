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
