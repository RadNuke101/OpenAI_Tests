def return_second_input(data):
    output = []
    for item in data:
        if 'USA' in item[1]:
            output.append(item[1])
        else:
            output.append(', USA')
    return output
