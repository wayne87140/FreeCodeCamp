import re

def get_operand(problems, operand_order):
    output_operands = []
    if len(problems)>5:
        return 'Error: Too many problems.'
    
    if operand_order == 1:
        pattern = r'^[1-9][0-9]*\b'
    if operand_order == 2:
        pattern = r'\b[1-9][0-9]*$'

    for problem in problems:
        try:
            match_operand = re.search(pattern, problem).group()
        except AttributeError:  # no result was found
            return 'Error: Numbers must only contain digits.'
        else:
            if len(match_operand)>4:
                return 'Error: Numbers cannot be more than four digits.'
            output_operands.append(match_operand)
    return output_operands


def get_operator(problems):
    output_operators = []
    pattern = r'\d\s?([+-])\s?\d'
    for problem in problems:
        try:
            match_operator = re.search(pattern, problem).group(1)
        except AttributeError:
            return "Error: Operator must be '+' or '-'."
        else:
            output_operators.append(match_operator)
    return output_operators

def get_errors(*arg):
    errors = set()
    for operator_or_operand in arg:
        if isinstance(operator_or_operand, str):
            errors.add(operator_or_operand)
    merge_errors = '\n'.join(errors)
    return merge_errors

def get_AddOrSubResult(first_operands, operators, second_operands):
    calculated_results = []
    for index, operator in enumerate(operators):
        if operator=='+':
            current_cal_result = int(first_operands[index]) + int(second_operands[index])
            
        if operator=='-':
            current_cal_result = int(first_operands[index]) - int(second_operands[index])

        calculated_results.append(str(current_cal_result))
    return calculated_results

def format_str(first_operands, operators, second_operands, cal_results=None):
    dash_lengths = [max(len(element1), len(element2))+2 for (element1, element2) in zip(first_operands, second_operands)]
    for index, dash_length in enumerate(dash_lengths):
        first_operands[index] = first_operands[index].rjust(dash_length)
        second_operands[index] = operators[index]+' '*(dash_length-1-len(second_operands[index]))+second_operands[index]
        if cal_results:
            cal_results[index] = cal_results[index].rjust(dash_length)


    first_line = '    '.join(first_operands)+'\n'
    second_line = '    '.join(second_operands)+'\n'
    third_line = '    '.join(['-'*dash_length for dash_length in dash_lengths])

    formatted_str = first_line + second_line + third_line
    if cal_results:
        formatted_str +='\n'+'    '.join(cal_results)+'\n'

    return formatted_str

def arithmetic_arranger(problems:list, display_answer=False)->str:
    first_operands = get_operand(problems, 1)
    second_operands = get_operand(problems, 2)
    operators = get_operator(problems)
    print(first_operands, second_operands, operators, sep='\n')
    merge_errors = get_errors(first_operands, second_operands, operators)

    if merge_errors:
        return merge_errors

    if display_answer:
        cal_results = get_AddOrSubResult(first_operands, operators, second_operands)
        return format_str(first_operands, operators, second_operands, cal_results) 
    else:
        return format_str(first_operands, operators, second_operands)    


if __name__ =="__main__":
    
    # first_operands = ['32', '3801', '45', '123']
    # operators = ['+', '-', '+', '+']
    # second_operands = ['698', '2', '43', '49']
    # print(get_AddOrSubResult(first_operands, operators, second_operands))
    # cal_results = ['730', '3799', '88', '172']
    # print(format_str(first_operands, operators, second_operands, cal_results))
    # print(get_operator(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    # print(arithmetic_arranger(["9999 + 698", "4789 - 2", "45 + 43", "123 + 49"], True))




    print(arithmetic_arranger(['32 - 6h55khl98', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))