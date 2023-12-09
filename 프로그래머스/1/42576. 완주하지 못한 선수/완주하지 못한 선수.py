def solution(participant, completion):
    comp_dict = dict()
    part_dict = dict()
    for i in completion:
        if comp_dict.get(i)!=None:
             comp_dict[i] +=1
        else:
            comp_dict[i]=1
        
    for j in participant:
        if part_dict.get(j)!=None:
             part_dict[j] +=1
        else:
            part_dict[j]=1
        
        
    for k in part_dict.keys():

        if comp_dict.get(k)==None or part_dict[k]!=comp_dict[k]:
            return k

