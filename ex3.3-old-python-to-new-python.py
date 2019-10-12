##########COPY DỮ LIỆU FILE CŨ SANG FILE MỚI
from sys import argv
from os.path import exists
# Sử dụng 3 tham biến tên script_py, tên file cũ, tên file mới
pythonfile, oldfile, newfile = argv

# Mở đường dẫn file cũ, rồi đọc nội dung file cũ, lưu nội dung file vào một biến
url_old_file = open(oldfile)
datafile = url_old_file.read()

# Mở đường dẫn file mới với thuộc tính Cho phép ghi, ghi dữ liệu mới vào file mới
url_new_file = open(newfile, 'w')
newfile = url_new_file.write(datafile)

#Đóng đường dẫn
url_old_file.close()
url_new_file.close()

"""
1. Trước khi đọc hay ghi vào file phải có động tác: Mở đường dẫn đến file đó.
2. Muốn ghi data mới vào file phải set thêm thuộc tính 'w', = open(oldfile,'w')
3. Sau khi mở url phải có động tác đóng url. url_file.close()

4.Trong hai ví dụ trên, hai file old_sample.txt và new_simple.txt đều cùng nằm chung thư mục với file tenfile.py
5. chạy lệnh sau ở chế độ Terminal python pythonfile.py  old_sample.txt  new_simple.txt
6. Nếu file cũ có dữ liệu thì dữ liệu sẽ bị xóa hết(tự động) trước khi dữ liệu mới ghi vào, trong chương trình này 

"""
