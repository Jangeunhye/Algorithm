def solution(n):
    i=2
    while n//i > 0:
        n=n//i
        i+=1
    return i-1
            