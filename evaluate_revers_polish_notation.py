#!/usr/bin/python

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                c = a + b
                stack.append(c)
            elif token == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                c = b - a
                stack.append(c)
            elif token == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                c = a * b
                stack.append(c)
            elif token == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                c = b / a
                stack.append(c)
            else:
                stack.append(int(token))
        return stack.pop()
                
    def evaluate(self, tokens):
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append(a+b)
            elif token == '-':
                stack.append(b-a)
            elif token == '*':
                stack.append(a*b)
            else:
                stack.append(int(1.0*b/a))
        return stack.pop()    



if __name__ == "__main__":
    s = Solution()
    a = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print s.evaluate(a)
