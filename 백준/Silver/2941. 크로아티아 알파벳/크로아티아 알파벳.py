s = input()
array = ["c=","c-","dz=","d-","lj","nj","s=","z="]
sum = 0
for i in range(len(array)):
    sum+=s.count(array[i])
    s = s.replace(array[i],"!")

sum+= (len(s)-s.count("!"))
print(sum)