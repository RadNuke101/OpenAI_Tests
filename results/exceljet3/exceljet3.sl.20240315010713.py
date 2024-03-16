def return_after_space(input_expression):
    return [item[0].split('= ')[1] for item in input_expression]

input_expression = [['year= 2016'], ['make= subaru'], ['model= outback wagon'], ['fuel economy= 25/33']]
output = return_after_space(input_expression)
print(output)
