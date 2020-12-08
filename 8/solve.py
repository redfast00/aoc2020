
class CPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.ip = 0
        self.seen = set()
        self.acc = 0
        self.first_solution = None

    def tick(self):
        self.seen.add(self.ip)
        self.first_solution = self.ip
        if self.ip not in range(len(self.instructions)):
            raise ValueError("found!")
        ins, arg = self.instructions[self.ip]
        self.ip += 1
        if ins == 'jmp':
            self.ip += arg - 1 # already incremented
        elif ins == 'nop':
            pass
        elif ins == 'acc':
            self.acc += arg
        return self.ip not in self.seen


def try_execute(instructions):
    c = CPU(instructions)
    try:
        while c.tick():
            pass
    except:
        return c.acc
    return None


with open('input') as infile:
    instructions = []
    for line in infile:
        ins, arg = line.strip().split(' ')
        if arg[0] == '+':
            arg = arg[1:]
        arg = int(arg)
        instructions.append((ins, arg))
    c = CPU(instructions)
    while c.tick():
        pass
    print(c.acc)

    for idx in range(len(instructions)):
        ins, arg = instructions[idx]
        if ins in ('nop', 'jmp'):
            if ins == 'nop':
                instructions[idx] = ('jmp', arg)
            elif ins == 'jmp':
                instructions[idx] = ('nop', arg)
            result = try_execute(instructions)
            if result:
                print(result)
            instructions[idx] = (ins, arg)



