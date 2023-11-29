n = int(input())
count = n 

for i in range(n):
    s = input()
    if(len(s)>2):
        for j in range(len(s)-1):
            if s.find(s[j])>s.find(s[j+1]):
                count-=1
                break
print(count)