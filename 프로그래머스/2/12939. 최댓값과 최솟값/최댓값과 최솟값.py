def solution(s):
    answer = ''
    array = list(map(int,s.split()))
    min_num = str(min(array))
    max_num = str(max(array))
    answer = min_num+" "+max_num
    
    return answer