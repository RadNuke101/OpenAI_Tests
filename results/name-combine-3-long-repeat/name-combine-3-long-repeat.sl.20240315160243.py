def first_letter_with_last_name(input_list):
    result = []
    for name in input_list:
        first_letter = name[0][0]
        last_name = name[1]
        result.append(f"{first_letter}. {last_name}")
    return result
