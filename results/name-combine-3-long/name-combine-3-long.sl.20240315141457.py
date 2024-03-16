def format_names(input_list):
    output_list = []
    for names in input_list:
        first_letter = names[0][0]
        formatted_name = f"{first_letter}. {names[1]}"
        output_list.append(formatted_name)
    return output_list
