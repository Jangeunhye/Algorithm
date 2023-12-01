def solution(participant, completion):
    part_hash = dict()
    comp_hash = dict()
    hashSum = 0

    # 1. participant해시 값 구하기
    for i in range(len(participant)):
        part_hash[hash(participant[i])] = participant[i]
        hashSum +=hash(participant[i])
        
    # 2. completion 해시값 구하기.
    for j in range(len(completion)):
        comp_hash[hash(completion[j])] = completion[j]
        hashSum -= hash(completion[j])
    
    return part_hash[hashSum]