def process_input(input_list):
    output_list = []
    for item in input_list:
        second_input = item[1]
        if "New York" in second_input:
            second_input = second_input.replace("New York", "NY")
        if "USA" not in second_input:
            second_input += ", USA"
        output_list.append(second_input)
    return output_list
