def return_number_from_input(input_list):
    output_list = []
    for sublist in input_list:
        output_list.append(sublist[0][4:-4])
    return output_list

input_list = [['<b>0.66<b>'], ['<b>0.409<b>'], ['<b>0.7268<b>']]
print(return_number_from_input(input_list))
