N, B = input().split()
B = int(B)
sum = 0

for i in range(len(N)):
    if(N[i].isdigit()):
        sum += B**(len(N)-i-1)*int(N[i])
    else:
        sum +=(B**(len(N)-i-1) )* (ord(N[i])-55)
print(sum)