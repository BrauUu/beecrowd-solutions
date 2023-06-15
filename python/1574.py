n = int(input())

for i in range(n):
    x = int(input())
    count = 0
    instructions = []
    
    for g in range(x):
        instruction = input()
        
        if instruction == "LEFT":
            count -= 1
        elif instruction == "RIGHT":
            count += 1
        else:
            p = instruction.split()
            instruction = instructions[int(p[2]) - 1]
            if instruction == "LEFT":
                count -= 1
            elif instruction == "RIGHT":
                count += 1
        instructions.append(instruction)
    
    print(count)
        