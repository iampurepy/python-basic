######### HÀM ĐỌC MỘT FILE  ex20.py ###########
"""
"""
from sys import argv

# thủ tục khi cần đọc/ghi một file. Đây cũng là dòng xác định
# số lượng biến cần truyền vào khi chạy lệnh terminal. Ở đây có 2 biến pythonpy và filedata
# do đó khi dùng lệnh terminal phải có đủ 2 biến: python pythonpy.py(biến 1) filedata(biến 2)
pythonpy, filedata = argv
# Read all data inside file.
def print_all(filename):
    print(filename.read())

# Sau khi read() thi cursor không còn ở vị trí đầu tiên nữa.
# vì vậy phải trỏ con trỏ về vị trí đầu tiên của filedata cần đọc bằng hàm seek(0)

def cursorfile(filename):
    filename.seek(0)

# Hàm đọc từng dòng một trong filedata, bắt đầu từ dòng đầu tiên
# Sử dụng hàm readline(). Hàm readline() với hàm read() có gì khác nhau ?
# Hàm readline() là đọc theo dòng(hàng ngang) ngay khi phát hiện có chỗ xuống dòng (\n) thì không đọc nữa.
# Hàm read() đọc từ đến cuối toàn bộ file.
def print_a_line(line_data,URLfile):
    print(line_data, URLfile.readline())

# Lấy đường dẫn của file cần đọc. Rule: TRƯỚC KHI ĐỌC FILE/GHI FILE BAO GIỜ CŨNG PHẢI LẤY ĐƯỜNG DẪN
file_need_read = open(filedata)

print(open(filedata)) #Đây là đường dẫn tới file cần đọc.

# In ra 2 dòng đầu tiên trong filedata.

#line_data_number = 1: in dòng đầu tiên.
line_data_number = 1
print_a_line(line_data_number,file_need_read)
print("\n")
line_data_number += 1
print_a_line(line_data_number,file_need_read)




