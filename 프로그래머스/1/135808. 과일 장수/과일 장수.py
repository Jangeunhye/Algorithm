def solution(k, m, score):
    answer = 0
    array = []
    score = sorted(score)
    for i in range(len(score)//m):
        array.append([])
        for j in range(m):
            array[i].append(score.pop())
        answer += min(array[i])*m
    
    return answer