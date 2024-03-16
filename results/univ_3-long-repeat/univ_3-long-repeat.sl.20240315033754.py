def return_second_input(data):
    output = []
    for item in data:
        if "USA" not in item[1]:
            output.append(", USA")
        else:
            output.append(item[1])
    return output
