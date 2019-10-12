
###HƯỚNG DẪN SỬ DỤNG FUNCTION CƠ BẢN ex18.py##########
"""
Functions do three things:

1. They name pieces of code the way variables name strings and numbers.
2. They take arguments the way your scripts take argv.
3. Using 1 and 2, they let you make your own “mini-scripts” or “tiny commands.”
"""




def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2:{arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2:{arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing")
print_two("Zed", "Shaw")
print_two_again("Ngoc", "Thuan")
print_one("First!")
print_none()

"""
NOTES:
1. def print_two(*args): What does the * in *args do? That tells Python to take all the arguments to the function and then
put them in args as a list. It’s like argv that you’ve been using but for functions. It’s NOT NORMATLLY USED TOO OFTEN unless speciﬁcally needed.
2. Dùng terminal để chạy lệnh trên: python test.py 
"""
