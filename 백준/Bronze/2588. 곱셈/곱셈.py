a = int(input())
b = int(input())

#b의 백의자리
b_100 = b//100
#b의 십의 자리
b_10 = (b%100)//10
#b의 일의자리
b_1 =  (b%100)%10

three = a*b_1
four = a*b_10
five = a*b_100
print(three)
print(four)
print(five)
four = four*10
five = five*100
print(three+four+five)
