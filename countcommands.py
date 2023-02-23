# "!1" would trigger the execution of "ls", "!3" would repeat "mv", and "!6" would execute "!1" which in turn would trigger the execution of "ls".
def solution(commands):
    
    stack = []
    ls, cp, mv = 0,0,0
    myindex = []
    
    
    for command in commands:
    
        if command == "ls":
            ls +=1 
            
        if command == "cp":
            cp += 1
        if command == "mv":
            mv += 1
            
        if command[0]== "!":
            myindex.append(int(command[1:]))
        
    for i in myindex:
        if commands[i-1] == "ls":
            ls += 1
        if commands[i-1] == "cp":
            cp += 1
        if commands[i-1] == "mv":
            mv += 1

        if commands[i-1][0] == "!":
            myindex.append(int(commands[i-1][1:]))

    return [cp,ls,mv]

# Path: leetcode/countcommands.py
commands = ["ls", "cp", "mv", "mv", "mv", "!1", "!3", "!6"]
print(solution(commands))

