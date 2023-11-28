n = int(input())
array = list(map(int, input().split()))
v = int(input())
sum=0
for i in array:
  if(i==v):
    sum+=1

print(sum)