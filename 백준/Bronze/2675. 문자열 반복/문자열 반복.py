t = int(input())

for _ in range(t):
  r, s= input().split()
  r = int(r)

  for i in s:
    print(r*i,end="")
  print()