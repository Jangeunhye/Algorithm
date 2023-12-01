def solution(arr):
    answer = []
    last = 10
    for i in arr:
        if(last!=i):
            answer.append(i)
            last=i
    
    
    return answer