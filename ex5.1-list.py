#### LUYEN TAP MOT VAI THAO TAC VOI LIST  - SOME PRACTICES WITH LISTS Exercise 32 in book###
list_number = [1,2,3,4,5]
list_string = ['one','two','three','four','five']
list_number_and_string = [11,'oneone',22,'twotwo',33,'threethree']
list_empty = [] #adding item to this list later
for number in list_number:
    print(f"Item of list_number is: {number}")

for string_item in list_string:
    print(f"Item of list_string is: {string_item}")


#Adding item to the list_empty
#use range(). Note:The range() function only does numbers from the ﬁrst to the last, NOT INCLUDING THE LAST.
for i in range(0,6):
    print(f"Adding {i} to the list_empty")
    list_empty.append(i)
#Check item in list_empty after append()
for i in list_empty:
    print(f"Item of list_empty is: {i}")
    
    
    """
    LIST tương đương Array trong một số ngôn ngữ khác
    """
    
