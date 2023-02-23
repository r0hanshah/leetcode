def solution(inputString):
    a,b = 0, len(inputString)-1
    i=0
    while i < len(inputString):
        
        i+=1;
        if inputString[a] == inputString[b]:
            a += 1
            b -= 1
            print("IM HERE")
            
            if a==b:
                return True;
                break;
            if len(inputString)==1:
                return True;
            
    return False;
    # if (inputString[::]== inputString[::-1]):
    #     return True;
    # return False;

inputString = "hlbeeykoqqqqokyeeblh"

print(solution(inputString))