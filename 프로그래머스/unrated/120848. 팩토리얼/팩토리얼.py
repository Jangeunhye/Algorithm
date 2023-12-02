def solution(n):
    i=2
    while True:
        if(n//i>0):
            n=n//i
            i+=1
        else:
            break
    return i-1
            