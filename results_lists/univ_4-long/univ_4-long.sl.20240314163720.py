def return_second_input(data):
    result = []
    for item in data:
        if 'USA' in item[1]:
            result.append(item[1])
        else:
            result.append(', USA')
    return result
