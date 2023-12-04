def solution(l, t):
    # Your code here
    res = 0
    head = 0
    tail =-1
    length = len(l)
    while(tail<length):
        if (res<t):
            tail+=1
        elif(res>t and head < tail):
            head+=1
        if(l[head] == 0 and head<tail):
            head+=1
        elif(res==t and l[head] != 0):
            return [head,tail]
        res = sum(l[head:tail+1])    
    return [-1,-1]