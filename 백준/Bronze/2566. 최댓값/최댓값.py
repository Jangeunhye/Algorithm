max_num = 0 
max_location = [100,100]

for i in range(9):
  a = list(map(int,input().split()))
  temp = max(a)
  if(temp>=max_num):
    max_num = temp
    max_location= [i+1,a.index(max_num)+1]

print(max_num)
print(max_location[0],max_location[1])