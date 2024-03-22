def process_names(names):
    result = []
    for name in names:
        first_name = name[0].split()[0][0]
        last_name = name[0].split()[1]
        result.append(first_name + ' ' + last_name)
    return result

input_names = [['John Doe'], ['Mayur Naik'], ['Nimit Singh']]
output_names = process_names(input_names)
print(output_names)
