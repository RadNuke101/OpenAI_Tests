def format_names(names):
    return [f"{name[0][0]} {name[0].split()[1]}" for name in names]

input_data = [['John Doe'], ['Mayur Naik'], ['Nimit Singh']]
output = format_names(input_data)
print(output)
