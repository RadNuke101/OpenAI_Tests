def return_second_input(data):
    output = []
    for item in data:
        if len(item) > 1 and "USA" not in item[1]:
            output.append(", USA")
        else:
            output.append(item[1])
    return output
