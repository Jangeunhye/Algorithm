n, m = map(int, input().split())
n_temp = []
m_temp = []

n_list = []
m_list = []
final_list = []

for i in range(n):
  n_temp = list(map(int, input().split()))
  n_list.append(n_temp)

for j in range(n):
  m_temp= list(map(int, input().split()))
  m_list.append(m_temp)


for i in range(n):
  final_list.append([])
  for j in range(m):
    print(n_list[i][j]+m_list[i][j],end=" ")
  print()
