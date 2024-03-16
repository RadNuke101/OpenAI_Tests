def get_first_word(input_list):
    output_list = []
    for sublist in input_list:
        output_list.append(sublist[0].split()[0])
    return output_list
