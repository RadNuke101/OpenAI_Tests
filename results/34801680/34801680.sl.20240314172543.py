def extract_names(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('= ')[1])
    return output_list

# Test the function with the given input
input_list = [['Name= ABC Retailers'], [' ame= XYZ Suppliers']]
print(extract_names(input_list))
