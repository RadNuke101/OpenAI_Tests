def check_overhead(input_list):
    output = []
    for item in input_list:
        if 'overhead' in item[0]:
            output.append('false')
        else:
            output.append('true')
    return output

input_list = [['some project,other project'], ['some project'], ['overhead'], ['some project, overhead'], ['some project, other, boo']]
print(check_overhead(input_list))
