def check_problem(num1, num2, operator):
    try: 
        num1 = int(num1)
        num2 = int(num2)
    except:
        return 'Error: Numbers must only contain digits'
    if abs(num1) > 9999 or abs(num2) > 9999:
        return 'Error: Numbers cannot be more than four digits'
    if operator not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
    return ''


def calculator(num1, num2, operator):
    n_1 = int(num1)
    n_2 = int(num2)
    if operator == '+':
        return str(n_1 + n_2)
    return str(n_1 - n_2)


def arithmetic_arranger(problems, calculate = False):
    if len(problems) > 5:
        return('Error: Too many problems.')
    line1 = line2 = line3 = line4 = ''
    margin = '    '
    for problem in problems:
        num1, operator, num2 = problem.split()
        is_ok = check_problem(num1, num2, operator)
        if not is_ok:
            return is_ok
        length = max(len(num1), len(num2))
        line1 += num1.rjust(length + 2) + margin
        line2 += operator + ' ' + num2.rjust(length) + margin
        line3 += '-' * (length + 2) + margin
        if calculate:
            line4 += calculator(num1, num2, operator).rjust(length + 2) + margin
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return arranged_problems