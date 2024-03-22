def rearrange_names(input_list):
    output_list = []
    for pair in input_list:
        first_name = pair[0].split(',')[1]
        last_name = pair[0].split(',')[0]
        output_list.append(f'{first_name},{last_name}')
    return output_list

input_list = [['chang,amy'], ['smith,bobby'], ['lennox,aaron']]
output = rearrange_names(input_list)
print(output)
