def delete_last_phrase(input_str):
    # Split the input string by space and store the words in a list
    str_list = input_str.split()
    # Check if the last word is all capitalized
    if str_list[-1].isupper():
        # If yes, remove the last word from the list
        str_list.pop()
    # Join the list back into string with a space between words
    output_str = " ".join(str_list)
    # Return the output string
    return output_str