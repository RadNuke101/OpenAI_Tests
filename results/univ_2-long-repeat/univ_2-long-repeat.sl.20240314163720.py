def format_input(input_list):
    output_list = []
    for item in input_list:
        if "USA" not in item[1]:
            output_list.append(item[0] + ", " + item[1] + ", USA")
        else:
            output_list.append(item[0] + ", " + item[1])
    return output_list
