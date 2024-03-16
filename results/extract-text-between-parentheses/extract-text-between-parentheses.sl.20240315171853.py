def extract_text(input_list):
    return [x[0].split('<')[1].split('>')[0] for x in input_list]

# Test the function with the provided input
input_list = [['Jones <60>'], ['Jones <57>'], ['Jones <55>']]
output = extract_text(input_list)
print(output)
