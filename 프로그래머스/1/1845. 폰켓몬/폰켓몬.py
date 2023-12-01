def solution(nums):
    temp = set(nums)
    answer=0
    
    for i in range(len(nums)//2):
        temp.pop()
        answer+=1
        if(len(temp)<=0):
            break
        
    return answer