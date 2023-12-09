def solution(emergency):
    order = []
    sorted_emergency = sorted(emergency,reverse=True)
    
    for i in range(len(emergency)):
        order.append(sorted_emergency.index(emergency[i])+1)
    return order