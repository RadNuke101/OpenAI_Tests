def return_after_space(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('= ')[1])
    return output_list

input_list = [['year= 2016'], ['make= subaru'], ['model= outback wagon'], ['fuel economy= 25/33']]
print(return_after_space(input_list))
