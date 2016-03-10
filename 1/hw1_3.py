import sys
import re


def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def infix_to_postfix(expr):
    priority = {'_': 1, '+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
    infixList = expr.split()
    position = 0
    RPN = []  # expression in reverse polish notation
    operators = []  # stack of operators
    while len(infixList) > 0:
        token = infixList.pop(0)
        if isfloat(token):
            RPN.append(float(token))
            continue
        else:
            if token == '(':
                operators.append('(')
            elif token == ')':
                while len(operators) != 0 and operators[-1] != '(':
                    RPN.append(operators.pop())
                if len(operators) == 0:
                    print "Not enough opening brackets"
                    return
                operators.pop()  # delete '('
            elif token == '**':  # power operator
                operators.append('**')
            else:  # default
                while len(operators) != 0 and operators[-1] != '(':
                    if priority[operators[-1]] >= priority[token]:
                        RPN.append(operators.pop())
                    else:
                        break
                operators.append(token)
    operators.reverse()
    RPN.extend(operators)
    return RPN


def evaluate(RPN):
    operands = []
    while len(RPN) != 0:
        token = RPN.pop(0)
        if type(token) == float:
            operands.append(token)
        else:
            right = operands.pop()
            left = operands.pop()
            if token == '+':
                operands.append(left + right)
            elif token == '-':
                operands.append(left - right)
            elif token == '*':
                operands.append(left * right)
            elif token == '/':
                operands.append(left / right)
            elif token == '**':
                operands.append(left ** right)
    return operands[0]


def main():
    expr = sys.stdin.readline()
    print evaluate(infix_to_postfix(expr))
    return

if __name__ == '__main__':
    main()
