def delete_suffix(input_string):
    """
    Function that removes everything after "-" in a string and returns it
    """
    if "-" in input_string:
        index = input_string.index("-")
        output_string = input_string[:index]
        return output_string
    else:
        return input_string