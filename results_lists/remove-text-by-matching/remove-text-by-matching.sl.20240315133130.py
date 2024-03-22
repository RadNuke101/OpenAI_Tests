def remove_dashes(input_list):
    output_list = []
    for sublist in input_list:
        output_list.append(sublist[0].replace('-', ''))
    return output_list

input_list = [['801-345-1987'], ['612-554-2000']]
print(remove_dashes(input_list))
