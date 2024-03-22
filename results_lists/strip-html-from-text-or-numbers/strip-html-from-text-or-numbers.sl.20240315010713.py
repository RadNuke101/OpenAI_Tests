def return_number_from_input(input_list):
    output = [item[0].strip('<b>').strip('</b>') for item in input_list]
    return output
