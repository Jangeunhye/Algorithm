a,b, c= map(int, input().split())
print(a,b,c)
d=1
while(d%a!=0 or d%b!=0 or d%c!=0):
    d=d+1
print(d)