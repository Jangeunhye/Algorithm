s = input()

second = 0

for i in s:
  if i in 'ABC':
    second = second + 3
  elif i in 'DEF':
    second = second + 4
  elif i in 'GHI':
    second = second + 5
  elif i in 'JKL':
    second = second + 6
  elif i in 'MNO':
    second = second + 7
  elif i in 'PQRS':
    second = second + 8
  elif i in 'TUV':
    second = second + 9
  elif i in 'WXYZ':
    second = second + 10

print(second)