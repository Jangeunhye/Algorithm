a,b,c = map(int, input().split())
# print( a if (a<b and a<c) else (b if b<c else c))

print((a if a<b else b) if (a if a<b else b) < c else c)

