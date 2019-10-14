i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
print("The numbers: ")
for num in numbers:
    print(num)

"""
1. What’s the difference between a for-loop and a while-loop? A for-loop can only iterate
(loop) “over” collections of things. A while-loop can do any kind of iteration (looping) you
want. However, while-loops are harder to get right, and you normally can get many things
done with for-loops.

2. Sử dụng print() để kiểm tra điều khiển vòng lặp. 
put print statements all over the loop printing out where in the loop Python is running and what the variables
are set to at those points. Write print lines before the loop, at the top of the loop, in the
middle, and at the bottom. Study the output and try to understand the jumping that’s going on.
"""
