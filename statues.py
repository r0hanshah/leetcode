def solution(statues):
    statues.sort();
    currentnum = statues[0]
    sums = 0;
    for index,num in enumerate(statues):
        if num> currentnum:
            
            if num != currentnum+1:
                sums += (statues[index] - statues[index-1])-1;
                currentnum = num;
                
            
            else:
                currentnum= num
    return sums;
statues = [6, 2, 3, 8]

print(solution(statues))