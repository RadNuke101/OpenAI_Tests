def return_numbers_from_input(input_data):
    output = [item[0].strip('<b>').strip('</b>') for item in input_data]
    return output

input_data = [['<b>0.66<b>'], ['<b>0.409<b>'], ['<b>0.7268<b>']]
output_data = return_numbers_from_input(input_data)
print(output_data)
