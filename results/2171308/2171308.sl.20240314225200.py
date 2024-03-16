def format_names(names):
    return [f"{name[0][0]} {name[0].split()[1]}" for name in names]

input_names = [['John Doe'], ['Mayur Naik'], ['Nimit Singh']]
output_names = format_names(input_names)
print(output_names)
