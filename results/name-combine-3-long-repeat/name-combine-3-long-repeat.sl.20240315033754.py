def first_letter_with_period(input_list):
    output = []
    for pair in input_list:
        first_letter = pair[0][0]
        output.append(f"{first_letter}. {pair[1]}")
    return output
