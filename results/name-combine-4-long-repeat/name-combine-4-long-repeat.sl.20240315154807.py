def format_names(names):
    result = []
    for name in names:
        result.append(name[1] + ', ' + name[0][0] + '.')
    return result
