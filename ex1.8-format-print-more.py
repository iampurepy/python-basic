dinhdang = "{} {} {} {}"
print(dinhdang .format(1,2,3,4))
print(dinhdang .format("one","two","three","four"))
print(dinhdang .format(True, False, False,True))
print(dinhdang .format(dinhdang, dinhdang, dinhdang, dinhdang))
print(dinhdang .format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
"""
Why do I have to put quotes around "one" but not around True or False? Python recognizes
True and False as keywords representing the concept of true and false. If you put quotes
around them then they are turned into strings and won’t work. You’ll learn more about how
these work in Exercise 27.
"""
