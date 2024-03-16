def get_initials(input_list):
    initials = []
    for item in input_list:
        words = item[0].split()
        initials.append(words[0][0].upper() + '.' + words[1][0].upper() + '.')
    return initials
