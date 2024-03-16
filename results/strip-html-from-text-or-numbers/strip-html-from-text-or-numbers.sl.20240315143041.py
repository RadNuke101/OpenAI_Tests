def return_number_from_input(input):
    return [item[0].strip('<b>').strip('</b>') for item in input]

input = [['<b>0.66<b>'], ['<b>0.409<b>'], ['<b>0.7268<b>']]
output = return_number_from_input(input)
print(output)
