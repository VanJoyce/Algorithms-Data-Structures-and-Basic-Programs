from math import pow

operators = ["+", "-", "*", "/", "^"]
parentheses = ["(", ")"]

def tokenization(expr):
    tokens = []
    number = ""
    for char in expr:
        if char in operators or char in parentheses:
            if number == "":
                tokens.append(char)
            else :
                number = float(number)
                tokens.append(number)
                tokens.append(char)
                number = ""
        elif char not in operators and char not in parentheses and char != " ":
            number += char
    if number != "":
        number = float(number)
        tokens.append(number)
    return tokens

def has_precedence(op1, op2):
    if op1 == "^" and (op2 == "*" or op2 == "/" or op2 == "+" or op2 == "-"):
        return True
    elif (op1 == "*" or op1 == "/") and (op2 == "+" or op2 == "-"):
        return True
    else :
        return False

def simple_evaluation(tokens):
    result = 0.0
    while len(tokens) != 1:
        op2 = "+"
        op_index = 1
        for t in tokens:
            if t in operators:
                if has_precedence(t, op2) == True:
                    op_index = tokens.index(t)
                    op2 = t
        operator = tokens[op_index]
        num1, num2 = tokens[op_index - 1], tokens[op_index + 1]
        if operator == "^":
            value = pow(num1,num2)
        elif operator == "*":
            value = num1 * num2
        elif operator == "/":
            value = num1 / num2
        elif operator == "+":
            value = num1 + num2
        elif operator == "-":
            value = num1 - num2
        tokens[op_index + 1] = value
        del tokens[op_index - 1 : op_index + 1]
    result = tokens[0]
    return result

def complex_evaluation(tokens):
    result = 0.0
    t = 0
    while t < len(tokens) and len(tokens) != 1:
        if tokens[t] == "(":
            opening_index = t
            t += 1
        elif tokens[t] == ")":
            closing_index = t
            bracket = tokens[opening_index + 1 : closing_index]
            value = simple_evaluation(bracket)
            tokens[closing_index] = value
            del tokens[opening_index : closing_index]
            t = 0                                       
        else :
            t += 1
    result = simple_evaluation(tokens)
    return result

def evaluation(string):
    tokens = tokenization(string)
    if "(" in string and ")" in string:
        result = complex_evaluation(tokens)
    else :
        result = simple_evaluation(tokens)
    return result
