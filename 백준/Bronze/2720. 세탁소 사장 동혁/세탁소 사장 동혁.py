q, d,n,p = 0,0,0,0
t = int(input())
for i in range(t):
    c = int(input()) 
    array = [25,10,5,1]
    for j in array:
        print(c//j,end=" ")
        c = c%j
    print()

