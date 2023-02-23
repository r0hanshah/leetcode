def romanToInt(s):
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        maxindex = len(s)-1
        for index,char in enumerate(s):

            if index == maxindex and roman[char] <= roman[s[index-1]]:
                sum += roman[char]
                break
            if index+1 == len(s):
                continue
        #     I
            if (roman[s[index]] == 1) and (roman[s[index+1]]== 5):
                sum += 4
                continue
            if (roman[s[index]] == 5) and (roman[s[index-1]]== 1) and (index != 0):
                continue

            if (roman[s[index]] == 1) and (roman[s[index+1]]== 10):
                sum += 9
                continue
            if (roman[s[index]] == 5) and (roman[s[index-1]]== 1) and (index != 0):
                continue

                # X 
            if (roman[s[index]] == 10) and (roman[s[index+1]]== 50):
                sum += 40
                continue
            if (roman[s[index]] == 50) and (roman[s[index-1]]== 10) and (index != 0):
                continue
            if (roman[s[index]] == 10) and (roman[s[index+1]]== 100):
                sum += 90
                continue
            if (roman[s[index]] == 100) and (roman[s[index-1]]== 10) and (index != 0):
                continue

                # C
            if (roman[s[index]] == 100) and (roman[s[index+1]]== 500):
                sum += 400
                continue
            if (roman[s[index]] == 500) and (roman[s[index-1]]== 100) and (index != 0):
                continue
            if (roman[s[index]] == 100) and (roman[s[index+1]]== 1000):
                sum += 900
                continue
            if (roman[s[index]] == 1000) and (roman[s[index-1]]== 100) and (index != 0):
                continue

            

            else:
                sum += roman[char]
            
        return sum

s= "LXXIX"

print(romanToInt(s))