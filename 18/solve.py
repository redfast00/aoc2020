expressions = []

def find_closing_bracket(s):
    open_brackets = 0
    for idx, char in enumerate(s):
        if char == '(':
            open_brackets += 1
        elif char == ')':
            open_brackets -= 1
        if open_brackets == 0:
            return s[1:idx], s[idx+2:]
    else:
        print(s)
        print("no closing bracket")

def parse_expression(s):
    if not s:
        return []
    # print(f'{s=}')
    first = s[0]
    if first.isdigit() or first == '+' or first == '*':
        part = s.split(' ', 1)
        current = [int(part[0]) if part[0].isdigit() else part[0]]
        if len(part) == 1:
            return current
        return current + parse_expression(part[1])
    elif first == '(':
        inner, rest = find_closing_bracket(s)
        return [parse_expression(inner)] + parse_expression(rest)

def ret_decorator(func):
    def wrapper(*args, **kwargs):
        print(*args, kwargs)
        res = func(*args, **kwargs)
        print(res)
        return res
    return wrapper


def evaluate_first(l):
    res = 0
    cur_op = None
    for val in l:
        # print(f'{res=}')
        # print(f'{val=}')
        if isinstance(val, int):
            if not cur_op:
                res = val
            else:
                res = cur_op(res, val)
        elif val == '*':
            cur_op = (lambda x,y: x*y)
        elif val == '+':
            cur_op = (lambda x,y: x+y)
        elif isinstance(val, list):
            executed = evaluate_first(val)
            if not cur_op:
                res = executed
            else:
                res = cur_op(res, executed)
    return res


def evaluate_second(l):
    processed = []
    for val in l:
        # print(val)
        # print(f'{processed=}')
        # print(' ')
        if isinstance(val, int):
            if not processed:
                processed = [val]
            elif processed[-1] == '+':
                _, num = processed.pop(), processed.pop()
                processed.append(num + val)
            elif processed[-1] == '*':
                processed.append(val)
        elif isinstance(val, list):
            evaluated = evaluate_second(val)
            if not processed:
                processed = [evaluated]
            elif processed[-1] == '+':
                _, num = processed.pop(), processed.pop()
                processed.append(num + evaluated)
            elif processed[-1] == '*':
                processed.append(evaluated)
        else:
            processed.append(val)
    return evaluate_first(processed)

total_first = 0
total_second = 0

with open('input') as infile:
    for line in infile:
        expr = parse_expression(line.strip())
        total_first += evaluate_first(expr)
        total_second += evaluate_second(expr)

print(total_first)
print(total_second)