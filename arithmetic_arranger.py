import re
def arithmetic_arranger(problems, show_answers = False):

    if len(problems) > 5:
        return f"Error: Too many problems."

    arranged_problems = ''
    first_line = ''
    second_line = ''
    calculation = ''
    lines = ''
    for prob in problems:
        print(f"Prob: ", {prob})
        # formatted_prob = ''
        if(prob.find('+') == -1 and prob.find('-') ==-1):
            return f"Error: Operator must be '+' or '-'."
        if(re.search('[a-zA-Z]', prob) != None):
            return f"Error: Numbers must only contain digits."
        split_prob = prob.split(' ')
        for e in split_prob:
            if (len(e)>4):
                return f"Error: Numbers cannot be more than four digits."
        
        first_num = split_prob[0]
        operator = split_prob[1]
        second_num = split_prob[2]
        max_len = max(len(first_num),len(second_num)) +2
        
        if operator == '+':
            sum = str(int(first_num) + int(second_num)) 
        elif operator == '-':
            sum = str(int(first_num) - int(second_num)) 
        line = ''
        top = str(first_num).rjust(max_len) 
        bottom  = operator + str(second_num).rjust(max_len - 1)
        sum_line = sum.rjust(max_len)
        for s in range(max_len):
            line += '-'

        if prob != problems[-1]:
            first_line += top + '    '            
            second_line += bottom + '    '
            lines += line + '    '
            calculation += sum_line + '    '
        else:
            first_line += top             
            second_line += bottom 
            lines += line
            calculation += sum_line 

    if show_answers:
        arranged_problems = first_line +'\n'+second_line +'\n'+lines +'\n' +calculation
    else:
        arranged_problems = first_line +'\n'+second_line +'\n'+lines
    # print(arranged_problems)
    return arranged_problems


