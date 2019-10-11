############ WRITE CONTENT TO A FILE AFTER DELETE PREVIOUS CONTENT #####################
# Command line: python test.py sample.txt
# Must have sample.txt in the same folder with test.py
from sys import argv
pythonfile, tenfile = argv
#OPEN FILE. COMMAND LINE MUST have two.
target = open(tenfile, 'w')
#DELETE ALL CONTENT PREVIOUS
target.truncate()
#WRITE NEW CONTENT
content = input("Nhap noi dung muon luu vao file: ")
target.write(content)
target.close()

"""
1. What does 'w' mean? If you use 'w' then you’re saying “open this ﬁle in ‘write’ mode,” thus the 'w' character. There’s
also 'r' for “read,” 'a' for “append,” and modiﬁers on these.

2. What modiﬁers to the ﬁle modes can I use? The most important one to know for now is the + modi-
ﬁer, so you can do 'w+', 'r+', and 'a+'. This will open the ﬁle in both read and write mode
and, depending on the character use, position the ﬁle in different ways.

3. Does just doing open(filename) open it in 'r' (read) mode? Yes, that’s the default for the
open() function.

4. Mở rộng code.
target.write("\n") xuống dòng mới trước khi ghi thêm nội dung.
target.write(content)
"""
