def extract_names(lst):
    return [x[0].split('= ')[1] for x in lst]

# Test the function with the given input
input_data = [['Name= ABC Retailers'], [' ame= XYZ Suppliers']]
output = extract_names(input_data)
print(output)
