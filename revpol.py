import sys


class Exp:
    def __init__(self, path):
        self.tokens = {}
        self.path = path

    def scanner(self):
        
        with open(f'{self.path}', 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            for line in lines:
                var, _, exp = line.split(maxsplit=2)
                self.tokens[var] = self.eval_exp(exp)
                

    def eval_exp(self,exp):
        stack = []

        for token in exp.split():
            if token not in '+-*/':
                if token.isdigit():
                    stack.append(int(token))
                elif token in self.tokens:
                    stack.append(self.tokens[token])
                


            else:
                rhs = stack.pop()
                lhs = stack.pop()
                if token ==  '+':
                    stack.append(lhs + rhs)
                elif token == '-':
                    stack.append(lhs - rhs)
                elif token == '*':
                    stack.append(lhs * rhs)
                elif token == '/':
                    token.append(lhs / rhs)

    

        return stack.pop()
                

    
    


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python revpol.py <filename>')

    else:
        path = sys.argv[1]
        exp = Exp(path)
        
        exp.scanner()

        print(exp.tokens)