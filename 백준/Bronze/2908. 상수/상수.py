a, b= map(list,input().split())
a.reverse()
b.reverse()
a = int(''.join(a))
b = int(''.join(b))

print(a if a>b else b)

