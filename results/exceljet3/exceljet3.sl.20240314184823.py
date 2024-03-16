def return_after_space(input_expression):
    return [expression[0].split('= ')[1] for expression in input_expression]

input_expression = [['year= 2016'], ['make= subaru'], ['model= outback wagon'], ['fuel economy= 25/33']]
output = return_after_space(input_expression)
print(output)
