def process_input(input_list):
    output = []
    for item in input_list:
        if "New York" in item[1]:
            output.append(item[1].replace("New York", "NY"))
        elif "USA" not in item[1]:
            output.append(item[1] + ", USA")
        else:
            output.append(item[1])
    return output
