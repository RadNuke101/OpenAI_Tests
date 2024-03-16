def process_names(names):
    result = []
    for name in names:
        first_letter = name[0][0]
        space_index = name[0].index(' ')
        result.append(first_letter + ' ' + name[0][space_index+1:])
    return result

input_names = [['John Doe'], ['Mayur Naik'], ['Nimit Singh']]
output_names = process_names(input_names)
print(output_names)
