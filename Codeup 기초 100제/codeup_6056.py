x, y = map(int, input().split())
x = bool(x)
y = bool(y)
print(((not x) and y) or (x and (not y) ))