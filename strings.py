def solution(inputArray):
    maxlength = 0
    newarray = []
    for strings in inputArray:
        if len(strings) > maxlength:
            maxlength = len(strings);
    
    for strings in inputArray:
        if len(strings) == maxlength:
           newarray.append(strings)
            
    return newarray;


inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(solution(inputArray))

