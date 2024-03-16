def process_input(input_list):
    output_list = []
    for item in input_list:
        if "New York" in item[1]:
            output_list.append(item[1].replace("New York", "NY"))
        elif "USA" not in item[1]:
            output_list.append(", USA")
        else:
            output_list.append(item[1])
    return output_list
