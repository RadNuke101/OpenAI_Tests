def remove_miles(input_list):
    output_list = [item[0].split()[0] for item in input_list]
    return output_list

input_list = [['736 miles'], ['1255 miles'], ['1221 miles'], ['790 miles']]
output = remove_miles(input_list)
print(output)
