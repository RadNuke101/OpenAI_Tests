def check_overhead(input_list):
    output_list = []
    for item in input_list:
        if 'overhead' in item[0]:
            output_list.append('false')
        else:
            output_list.append('true')
    return output_list

# Input
input_list = [['some project,other project'], ['some project'], ['overhead'], ['some project, overhead'], ['some project, other, boo']]

# Output
output_list = check_overhead(input_list)
print(output_list)
