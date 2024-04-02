N, B = input().split()
B = int(B)
sum = 0

if(N.isalnum()):
    for i in range(len(N)):
        if(N[i].isdigit()):
            # 숫자일때
            sum +=(B**(len(N)-i-1))*int(N[i])
            
        elif(N[i].isalpha()):
            # 숫자가 아닐때
            temp = ord(N[i])-55
            sum +=(B**(len(N)-i-1))*temp

print(sum)