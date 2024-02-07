class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()


def calculate(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "^": 
        return operand1 ** operand2
    elif operator == "**": 
        return operand1 ** operand2       


def postfixEval(expression):
    operators = ["+","-","*","/","^","**"]
    operandStack = Stack()
    tokenList = expression.split(" ")
    
    for token in tokenList:
      if token in operators: 
        operand2 = operandStack.pop()
        operand1 = operandStack.pop()
        result = calculate(token,operand1,operand2)
        operandStack.push(result)
      elif (token.isdigit()): 
        operandStack.push(float(token))
        
    return operandStack.pop()