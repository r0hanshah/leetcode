def solution(inputString):
    a,b = 0, len(inputString-1)

    while inputString[a] == inputString[b]:
        a += 1
        b -= 1
        
        if a==b:
            return True;
        else:
            return False;