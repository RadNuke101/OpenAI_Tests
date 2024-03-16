def return_number_from_input(input_list):
    output = [item[0][3:-4] for item in input_list]
    return output

input_list = [['<b>0.66<b>'], ['<b>0.409<b>'], ['<b>0.7268<b>']]
print(return_number_from_input(input_list))
