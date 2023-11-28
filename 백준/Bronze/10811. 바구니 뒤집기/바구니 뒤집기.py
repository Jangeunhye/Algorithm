n, m = map(int, input().split())

array = [i for i in range(1,n+1)]
for _ in range(m):
  i, j = map(int, input().split())
  temp = array[i-1:j]
  temp.reverse()
  array[i-1:j] = temp

for i in array:
  print(i, end=" ")