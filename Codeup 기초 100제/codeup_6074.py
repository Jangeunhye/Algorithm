char = input()
char_num = ord(char)
a_num = ord('a') 
for i in range(a_num,char_num+1):
    print(chr(i),end=" ")