def rearrange_names(input_list):
    output_list = []
    for pair in input_list:
        name = pair[0].split(',')
        output_list.append(name[1] + ',' + name[0])
    return output_list

input_list = [['chang,amy'], ['smith,bobby'], ['lennox,aaron']]
output = rearrange_names(input_list)
print(output)
