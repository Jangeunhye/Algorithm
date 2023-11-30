q, d,n,p = 0,0,0,0
t = int(input())
for i in range(t):
  c = int(input())

  #쿼터
  q =c//25
  c = c%25

  #다임
  d = c//10
  c= c%10

  #니켈
  n = c//5
  c = c%5
  
  #페니
  p = c//1
  print(q,d,n,p)