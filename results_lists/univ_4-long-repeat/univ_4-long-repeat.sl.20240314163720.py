def return_second_input(data):
    result = []
    for item in data:
        second_input = item[1]
        if "USA" not in second_input:
            result.append(", USA")
        else:
            result.append(second_input)
    return result
