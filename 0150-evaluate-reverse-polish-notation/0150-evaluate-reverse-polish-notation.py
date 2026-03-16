class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:   # division
                    stack.append(int(float(a) / b))   # truncate toward zero
            else:
                stack.append(int(t))

        return stack.pop()