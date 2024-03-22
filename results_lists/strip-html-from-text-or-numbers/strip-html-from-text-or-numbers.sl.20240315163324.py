def return_number_from_input(input_list):
    return [item[0][4:-4] for item in input_list]

# Test the function
input_list = [['<b>0.66<b>'], ['<b>0.409<b>'], ['<b>0.7268<b>']]
print(return_number_from_input(input_list))  # Output: ['0.66', '0.409', '0.7268']
