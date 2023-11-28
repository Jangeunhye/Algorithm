array = [i for i in range(1,31)]
for i in range(28):
  num = int(input())
  array.remove(num)

print(min(array))
print(max(array))