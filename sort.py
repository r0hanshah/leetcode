def solution(a):
    b = []
    for elm in a:
        b.append(elm)

    
    a.sort()
    a = [i for i in a if i != -1]
    for index,num in enumerate(b):
        if num == -1:
            a.insert(index, num)
            
    return a
        

a = [-1, 150, 190, 170, -1, -1, 160, 180]
a = [i for i in a if i != -1]
print(a)

# print(solution(a))