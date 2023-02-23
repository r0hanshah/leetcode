def solution(n):
        new = str(n)
        index1 = len(new)//2
        
        firsthalf = new[0:index1]
        
        secondhalf = new[len(new)//2:]
        
        sum1 = 0
        sum2= 0
        for num in firsthalf:
            sum1 += int(num)
        for num in secondhalf:
            sum2+= int(num)
            
        if sum1 == sum2:
            return True
            
        else:
            print(firsthalf, secondhalf)
            print(sum1, sum2)
            return False

n = 1230
news = str(n)
index1 = len(news)//2 -1
print(  index1  )
print(news)

print(solution(n))