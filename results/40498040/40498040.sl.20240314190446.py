def check_overhead(input_list):
    output_list = []
    for item in input_list:
        if 'overhead' in item[0]:
            output_list.append('false')
        else:
            output_list.append('true')
    return output_list

# Test the function with the given input
input_list = [['some project,other project'], ['some project'], ['overhead'], ['some project, overhead'], ['some project, other, boo']]
output = check_overhead(input_list)
print(output)
