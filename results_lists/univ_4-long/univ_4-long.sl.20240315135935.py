def return_second_input(data):
    result = []
    for item in data:
        if len(item) > 1 and 'USA' not in item[1]:
            result.append(', USA')
        else:
            result.append(item[1])
    return result
