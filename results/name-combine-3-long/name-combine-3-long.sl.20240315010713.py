def format_names(names):
    result = []
    for name in names:
        first_letter = name[0][0]
        formatted_name = f"{first_letter}. {name[1]}"
        result.append(formatted_name)
    return result
