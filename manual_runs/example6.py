def first_letter(input_str):
    words = input_str.split()
    first_letter = words[0][0]
    return first_letter + " " + words[1]