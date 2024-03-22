def remove_dash(input):
    output = []
    for item in input:
        output.append(item[0].replace('-', ''))
    return output

input = [['801-345-1987'], ['612-554-2000']]
output = remove_dash(input)
print(output)
