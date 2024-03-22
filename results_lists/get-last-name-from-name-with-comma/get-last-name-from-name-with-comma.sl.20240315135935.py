def rearrange_names(input_list):
    output_list = []
    for item in input_list:
        name = item[0].split(',')
        rearranged_name = name[1] + ',' + name[0]
        output_list.append(rearranged_name)
    return output_list

input_list = [['chang,amy'], ['smith,bobby'], ['lennox,aaron']]
output = rearrange_names(input_list)
print(output)
