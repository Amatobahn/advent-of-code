def run(program, inputs, pc):
    num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3]
    i = pc
    input_idx = 0
    while program[i] != 99:
        modes = [int(x) for x in f"{program[i]:0>5}"[:3]][::-1]
        instruction = int(f"{program[i]:0>5}"[3:])
        operands = [program[i+x+1] if modes[x] else program[program[i+x+1]] for x in range(num_of_operands[instruction])]
        if instruction == 1:
            program[program[i+3]] = operands[0] + operands[1]
        elif instruction == 2:
            program[program[i+3]] = operands[0] * operands[1]
        elif instruction == 3:
            program[program[i+1]] = inputs[input_idx]
            input_idx+=1
        elif instruction == 4:
            return (operands[0], i+2)
        elif instruction == 5:
            i = (operands[1] - 3) if operands[0]!=0 else i
        elif instruction == 6:
            i = (operands[1] - 3) if operands[0]==0 else i
        elif instruction == 7:
            program[program[i+3]] = int(operands[0] < operands[1])
        elif instruction == 8:
            program[program[i+3]] = int(operands[0] == operands[1])
        i += num_of_operands[instruction] + 1
    return [False,False]

def set_sequence(line, settings, feedback):
    prev = 0
    program = [int(x) for x in line]
    amplifiers = [[program.copy(),0] for _ in range(5)]
    for i in range(5):
        output, pc = run(amplifiers[i][0], [settings[i],prev], amplifiers[i][1])
        prev = output
        amplifiers[i][1] = pc
    if not feedback: return prev
    i = 0
    while True:
        output, pc = run(amplifiers[i][0], [prev], amplifiers[i][1])
        if output == False: break
        prev = output
        amplifiers[i][1] = pc
        i = (i+1)%5
    return prev

def permute(arr, tmp, res, index):
    if index >= len(tmp):
        return res.append(tmp.copy())
    for i in range(len(arr)):
        tmp[index] = arr[i]
        permute(arr[:i]+arr[i+1:], tmp, res, index+1)

with open("puzzle_inputs/input_day_07.txt") as file:
    line = file.readline().split(",")
    res1, res2 = [], []
    permute(list(range(5)), list(range(5)), res1, 0)
    permute(list(range(5,10)), list(range(5,10)), res2, 0)
    print(max(set_sequence(line, per, False) for per in res1))
    print(max(set_sequence(line, per, True) for per in res2))