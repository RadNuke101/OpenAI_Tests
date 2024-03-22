def remove_miles(input_list):
    output_list = [item[0].split()[0] for item in input_list]
    return output_list
