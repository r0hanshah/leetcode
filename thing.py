def solution(sequence):
    
    for index ,num in enumerate(sequence):
        if index+1 == len(sequence):
            continue;
        if sequence[index] > sequence[index+1]:
            newlist = sequence;
            newlist.pop(index)
            # newlist= newlist[1::]
            for index,num in enumerate(newlist):
                if index+1 == len(newlist):
                    continue;
                if newlist[index] > newlist[index+1]:
                    return False;
                if newlist[index] == newlist[index+1]:
                    return False;
                if newlist[index] < newlist[index+1]:
                    return True;
    
        if sequence[index]==sequence[index+1]:
            return True;

sequence = [1, 3, 2, 1]
print(solution(sequence))