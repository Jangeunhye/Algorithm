# 3개의 주사위 입력받기
a, b, c= map(int, input().split())
# 같은 눈 3개  인지 확인
if (a==b):
  if(b==c):
    price = 10000+a*1000
  else:
    price = 1000 + a*100
elif (a==c):
    price = 1000 + a*100
else:
  if(b==c):
    price = 1000 + b*100
  else:
    price = max(a,b,c)*100


print(price)
