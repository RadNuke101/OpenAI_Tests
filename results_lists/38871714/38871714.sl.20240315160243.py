def remove_angle_brackets(input_data):
    output = []
    for item in input_data:
        new_item = item[0].replace('<', '').replace('>', '')
        output.append(new_item)
    return output

input_data = [['This is a <string>, It should be <changed> to <a> number.'], ['a < 4 and a > 0']]
print(remove_angle_brackets(input_data))
