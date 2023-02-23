def solution(inputString):
    my = 0
    you= 0
    index1 =0
    
    newstring = ""
    for index,char in enumerate(inputString):

        if char == "(":
            my = index+1
            index1 = index
            continue
        if char == ")":
            you = index-1
            continue
        if index >= my and index <= you:
            continue
        else:
            newstring += char

    substr = inputString[my:you+1]


    newstring += char
    newstring.insert(index1,substr[::-1])

          
    
    
    return newstring

inputString = "foo(bar)baz"
print(solution(inputString))