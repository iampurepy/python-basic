## Kiem tra thao tac don gian da hoc
print("Let's practice everything I have learnt")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
x = 10**2-10
print(f"Gia tri cua x {x}")

# Một function có thể trả về nhiều kết quả. 
def cong_thuc(bienso):
    bien1 = bienso*9
    bien2 = bien1/5
    bien3 = bien2/2
    return bien1, bien2, bien3
biensox = 100
bien1, bien2, bien3 = cong_thuc(biensox)
print("Bien so x:={}".format(biensox))

#Cách một: f"Chuỗi-string {} {}
print(f"Ket qua tra ve tu ham congthuc() la {bien1}, {bien2}, {bien3}")

diem_bat_dau = biensox
motdangketquakhac = cong_thuc(diem_bat_dau)

#Cách hai:format()
# format(*motdangketquakhac): this is an easy way to apply a list to a format string
print("Ket qua tra ve tu ham congthuc() la {}, {}, {}".format(*motdangketquakhac))

"""
 1. Remember that inside the function the variable is temporary. When you return it 
    then it can be assigned to a variable for later.
    
 2.Cách đọc code: đọc từ dưới lên trên. Start at the last line. Compare that line in your ﬁle
to the same line in mine. Once it’s exactly the same, move up to the next line. Do this until you
get to the ﬁrst line of the ﬁle.
"""

