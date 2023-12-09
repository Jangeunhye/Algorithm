def solution(participant, completion):
    comp_dict = dict()
    part_dict = dict()
    for i in completion:
        comp_dict[i]=1 if comp_dict.get(i)==None else comp_dict[i]+1
        
    for j in participant:
        part_dict[j]=1 if part_dict.get(j)==None else part_dict[j]+1
        
        
    for k in part_dict.keys():
        if comp_dict.get(k)!=part_dict.get(k):
            return k

