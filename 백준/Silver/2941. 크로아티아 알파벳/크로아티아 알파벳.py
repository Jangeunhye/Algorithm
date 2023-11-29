s = input()
array = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in range(len(array)):
    s = s.replace(array[i],"!")

print(len(s))