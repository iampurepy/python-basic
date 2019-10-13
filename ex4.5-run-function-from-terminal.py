############# Call function() from terminal #########################
### Thực hiện chức năng của hàm bằng cách ###########################
### GỌI CHÍNH XÁC TÊN  HÀM (KHÔNG CẦN GÕ CHÍNH XÁC TÊN BIẾN) thông qua terminal ##########
### ĐÃ ĐƯỢC ĐỊNH NGHĨA TRƯỚC ĐÓ, TRỪ TÊN BIẾN TRUYỀN VÀO HÀM LẦN ĐẦU TIÊN #########
### THỰC HIỆN:
# python
# import test2
# bienstring = "Toi di hoc lop mot", không cần gõ chính xác vì bienstring là biến truyền giá trị vào hàm
# words (KHÔNG CẦN phải gõ chính xác, có thể words hoặc wordxxx...) = test2.split_sentence(bienstring)

def split_sentence(stuff):
    words = stuff.split(' ')
    # Split() a string into a list where each word is a  item
    return words


def sort_string(words):
    return sorted(words) #The sorted() function returns a sorted list of the specified iterable object.

def print_first_word(words):
    first_word = words.pop(0)
    print(first_word)

def print_last_word(words):
    last_word =words.pop(-1)
    print(word)

def sort_sentence(sentence):
    sentence_sorted = split_string(sentence)
    return sort_string(sentence_sorted)

def print_first_and_last(sentence):
    words = split_string(sentence)
    print_first_word(words)
    print_last_word(words)

"""
Hướng dẫn chạy lệnh thực hiện hàm:
1.Trong Pycharm chọn terminal
2. Gõ python 
3. Gõ import test2 (ở đây test2 là test2.py là phần file py trong pycharm đang lưu code)
3. GÕ CHÍNH XÁC TÊN HÀM, TÊN BIẾN ĐÃ ĐỊNH NGHĨA TRƯỚC ĐÓ.nếu gõ không tuyệt-đối-chính-xác sẽ bị lỗi.
4. Thực hiện lần lượt các lệnh như trong hướng dẫn của book
5. Thoát khỏi terminal bằng quit() hoặc Ctr+Z
"""

