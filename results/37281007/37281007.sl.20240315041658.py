def check_expression(input_list):
    output = []
    for exp, letter in input_list:
        if letter in exp:
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['ABC', 'D'], ['ABC', 'BC']]
print(check_expression(input_list))
