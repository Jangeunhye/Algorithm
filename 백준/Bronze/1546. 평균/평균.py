n = int(input())
array = list(map(int, input().split()))
max_score = max(array)
sum = 0
for i in range(n):
  new_score = array[i]/max_score*100
  sum += new_score
print(sum/n)
