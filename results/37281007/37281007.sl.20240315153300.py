def check_expression(input_list):
    output = []
    for exp, check in input_list:
        if check in exp:
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['ABC', 'D'], ['ABC', 'BC']]
print(check_expression(input_list))
