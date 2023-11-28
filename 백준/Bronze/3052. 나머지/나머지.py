array = []
for _ in range(10):
  num = int(input())
  array.append(num%42)

my_set = set(array)

print(len(my_set))