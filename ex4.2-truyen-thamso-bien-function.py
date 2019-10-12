###Different ways we’re able to give the function the values###############
"""
1. We can give it straight numbers.
2. We can give it variables.
3. We can give it math.
4. We can even combine math and variables.
"""
def function_given_value(x1, x2):
    print(f"Bien thu nhat: = {x1}")
    print(f"Bien thu hai:= {x2}")
    print("Khoang trong. \n")

#1. We can give it straight numbers.
print("Give function Values")
function_given_value(20,30)

#2. We can give it variables.
print("Give function Variables")
b1 = 201
b2 = 202
function_given_value(b1, b2)

#3. We can give it math.
print("Give function math expression")
function_given_value(20+10,30+10)

#4. We can even combine math and variables.
print("Give function Value + Variables")
function_given_value(b1+9, b2+8)

"""
TÌM HIỂU THÊM:
1. there’s a theoretically inﬁnite number of ways to call any function.
2. Thêm chú thích cho mỗi câu lẹnh của hàm để dễ hiểu hơn.
3. Biến cục bộ trong hàm và biến toàn cục (later).
4. Truyền được số lượng bao nhiêu biến vào hàm. (Is there a limit to the number of arguments a function can have? It depends on the version of Python
and the computer you’re on, but it is fairly large. The practical limit though is about ﬁve argu-
ments before the function becomes annoying to use.)
5. call a function within a function. OK. Later 

"""

