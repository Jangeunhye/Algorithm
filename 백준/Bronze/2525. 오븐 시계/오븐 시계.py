A,B = map(int, input().split())
C = int(input())

minute = B+C
hour = (minute//60)+A
if(hour>=24):
  hour = hour-24
minute = (minute%60)

print(hour, minute)