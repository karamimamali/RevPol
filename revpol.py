import sys
import operator
import math

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def evaluate_rpn(expression: str) -> float:
    stack = []
    tokens = expression.strip().split()

    for token in tokens:
        if token in OPS:
            if len(stack) < 2:
                raise ValueError("Not enough operands")
            b = stack.pop()
            a = stack.pop()
            result = OPS[token](a, b)
            stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    
    return stack[0]

def run():
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if line.strip() == '':
                    continue
                try:
                    result = evaluate_rpn(line)
                    print(f"Line {line_number}: {result}")
                except Exception as e:
                    print(f"Line {line_number} Error: {e}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python revpol.py <filename>")
    else:
        run()
