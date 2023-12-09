def solution(nums):
    mydict= dict()
    for i in nums:
        mydict[i] = 1 if mydict.get(i)==None else mydict[i]+1
    return min(len(nums)/2, len(mydict))