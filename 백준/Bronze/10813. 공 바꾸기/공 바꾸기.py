n, m = map(int, input().split())
array = []
for i in range(n+1):
    array.append(i)

for j in range(m):
    a, b = map(int, input().split())
    temp = 0
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

for k in range(1,n+1):
    print(array[k],end=" ")