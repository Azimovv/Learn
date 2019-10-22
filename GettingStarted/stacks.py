# stacks are 'last in first out' data structures

from GettingStarted import stack as s

my_string = "Hello"
stack = s.Stack()

for c in my_string:
    stack.push(c)

new_string = ""
for i in range(len(my_string)):
    new_string += stack.pop()

print (new_string)


# problem: write program that tests string for balanced parentheses

# first solution
def balanced_par(expression):
    stack2 = []
    for c in expression:
        if c == '(':
            stack2.append(c)
        elif c == ')':
            if len(stack2) < 1:
                return False
            stack2.pop()
        if len(stack2) == 0:
            return True
        return False

# second solution (doesn't utilize a stack)
def balanced_par2(expression):
    is_balanced = 0
    for c in expression:
        if c == '(':
            is_balanced += 1
        elif c == ')':
            is_balanced -= 1
    if is_balanced == 0:
        return True
    else:
        return False

print (balanced_par("((()((()((()((((()))))"))
print (balanced_par2("((()((()((()((((()))))"))