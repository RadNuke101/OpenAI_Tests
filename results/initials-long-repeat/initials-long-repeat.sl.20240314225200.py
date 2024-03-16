def get_initials(input_list):
    initials = []
    for item in input_list:
        words = item[0].split()
        initials.append(f"{words[0][0]}.{words[1][0]}.")
    return initials
