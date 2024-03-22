def return_second_input(data):
    output = []
    for item in data:
        second_input = item[1]
        if "USA" not in second_input:
            output.append(", USA")
        else:
            output.append(second_input)
    return output
