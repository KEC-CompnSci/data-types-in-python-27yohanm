# Create the requested sentence by converting and combining these variables
# You may not add any additional string or numeric literals
# You can only use these variables, type conversion, and string concatenation

num_str_1 = "42"
num_str_2 = "13"
num_str_3 = "7"
word_1 = "robots"
word_2 = "built"
word_3 = "today"
word_4 = "were"



num_str_1 = "42"
num_int_1 = int(num_str_1)

num_str_2 = "13" 
num_int_2 = int(num_str_2)     

num_str_3 = "7" 
num_int_3 = int(num_str_3)

total_num= num_int_1 + num_int_2

total_num_str= str(total_num)


word_1 = " robots"
word_1_str = str(word_1)

word_2 = " built"
word_2_str= str(word_2)


word_3 = " today"
word_3_str= str(word_3)

word_4 = " were"
word_4_str= str(word_4)

sentence= total_num_str + word_1_str  + word_4_str  + word_2_str  + word_3_str

print(sentence)