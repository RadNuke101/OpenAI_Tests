def return_letters_after_last_slash(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('/')[-1])
    return output_list
