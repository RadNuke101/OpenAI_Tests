def extract_names(input_list):
    return [item[0].split('= ')[1] for item in input_list]

# Test the function with the provided input
input_list = [['Name= ABC Retailers'], [' ame= XYZ Suppliers']]
output = extract_names(input_list)
print(output)
