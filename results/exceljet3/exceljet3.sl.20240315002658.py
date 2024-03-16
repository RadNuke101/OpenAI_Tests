def return_after_space(input_list):
    return [item[0].split('= ')[1] for item in input_list]

input_list = [['year= 2016'], ['make= subaru'], ['model= outback wagon'], ['fuel economy= 25/33']]
output = return_after_space(input_list)
print(output)
