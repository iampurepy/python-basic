#############LUYỆN TẬP VỚI LIST -append(), join(), pop(),pop(i)#####################
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')
#Hàm string.split(' ') chia một string thành các từ.
#list = string.split(' ')
print("stuff = ", stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee",
"Corn", "Banana", "Girl", "Boy"]
print(more_stuff.pop())
#Hàm list.pop() nếu không có giá trị thì lấy phần tử cuối cùng của list
#Hàm list.pop(i) truy cập phần tử thứ i trong chuỗi

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)}")

# Các hàm với chuỗi
print("stuff[1] = ",stuff[1])
print("stuff[-1] = ",stuff[-1])
print(stuff.pop())
print(' . '.join(stuff))
print(' # '.join(stuff))
print(' # '.join(stuff[0:3]))
