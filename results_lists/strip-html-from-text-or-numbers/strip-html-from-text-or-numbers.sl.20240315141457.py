def return_number_from_input(input):
    output = [i[0][4:-4] for i in input]
    return output

input = [['<b>0.66<b>'], ['<b>0.409<b>'], ['<b>0.7268<b>']]
print(return_number_from_input(input))
