# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный. Пример:
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций. Пример:
# 1+2*3 => 7; 
# (1+2)*3 => 9;

def actions(a, b, operation): 
    return {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a / b}[operation](a, b)

def priority(text):
    # В выражении без скобок выполняем сначала */, затем +-
    delete = []
    for i in range(len(text)-1):
        if text[i] == '*':
            x = int(text[i-1])
            y = int(text[i+1])
            text[i+1] = actions(x, y, '*')
            delete.append(i-1)
            delete.append(i)
        elif text[i] == '/':
            x = int(text[i-1])
            y = int(text[i+1])
            text[i+1] = actions(x, y, '/')
            delete.append(i-1)
            delete.append(i)
        
    delete.reverse()
    for el in delete:
        text.pop(el)
    
    delete.clear()
    for i in range(len(text)-1):
        if text[i] == '+':
            x = int(text[i-1])
            y = int(text[i+1])
            text[i+1] = actions(x, y, '+')
            delete.append(i-1)
            delete.append(i)
        if text[i] == '-':
            x = int(text[i-1])
            y = int(text[i+1])
            text[i+1] = actions(x, y, '-')
            delete.append(i-1)
            delete.append(i)
    delete.reverse()
    for el in delete:
        text.pop(el)
    return text

def check_bracket(expression):
    # считаем только выражение в скобках 
    brackets = []
    index = []
    for i in range(len(expression)):
        if expression[i] == '(':
            index.append(i)
            for j in range(i+1, len(expression)):
                if expression[j] == ')':
                    index.append(j)
                    break
                brackets.append(expression[j])
    res = priority(brackets)
    expression[index[0]] = res[0]

    for i in range(index[1], index[0], -1):
        expression.pop(i)
    return expression

def calculator(data):
    # отделяем цифры от символов:
    # если цифра в нескольких ячейках, соединяем ее в одну
    pop_list = []
    for i in range (len(data)-1):
        if data[i].isdigit() and data[i+1].isdigit():
            data[i+1] = data[i] + data[i+1]
            pop_list.append(i)
    pop_list.reverse()
    for el in pop_list:
        data.pop(el)

    while '(' in data:
        check_bracket(data)
        
    return priority(data)
    
arithmetic_expression = input('Введите выражение для рассчета: ')
expression_list = [el for el in arithmetic_expression]
total = calculator(expression_list)
total = total[0]
print(f'Ответ = {total}')
