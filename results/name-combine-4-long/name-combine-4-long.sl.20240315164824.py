def format_names(names):
    formatted_names = []
    for name in names:
        formatted_name = name[1] + ', ' + name[0][0] + '.'
        formatted_names.append(formatted_name)
    return formatted_names
