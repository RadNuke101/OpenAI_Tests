def extract_info(input_data):
    output = []
    for item in input_data:
        output.append(item[0].split('= ')[1])
    return output

input_data = [['year= 2016'], ['make= subaru'], ['model= outback wagon'], ['fuel economy= 25/33']]
output = extract_info(input_data)
print(output)
