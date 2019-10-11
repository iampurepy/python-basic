#ex 15 in book
from sys import argv
script,filename = argv
txt = open(filename)
print(f"Here's your file {filename}:")
print(txt.read())

#txt.read() says, “Hey txt! Do your read command with no parameters!”
print("Typle the filename again:")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())
"""
1.Does txt = open(filename) return the contents of the ﬁle? No, it doesn’t. 
It actually makes something called a FILE OBJECECT. You can think of a ﬁle like an old tape drive that you saw on
mainframe computers in the 1950s or even like a DVD player from today. You can move around
inside them and then “read” them, but the DVD player is not the DVD the same way the ﬁle
object is not the ﬁle’s contents.

2. Why is there no error when we open the ﬁle twice? Python will not restrict you from opening a ﬁle
more than once, and sometimes this is necessary.

3. What does from sys import argv mean? For now just understand that sys is a package, and
this phrase just says to get the argv feature from that package. You’ll learn more about these
later.
"""
