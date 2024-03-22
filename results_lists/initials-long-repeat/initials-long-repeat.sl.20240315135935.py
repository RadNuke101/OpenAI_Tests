def generate_initials(input_list):
    initials = []
    for item in input_list:
        words = item[0].split()
        if len(words) >= 2:
            initials.append(f"{words[0][0]}.{words[1][0]}.")
    return initials
