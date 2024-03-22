def get_letters_after_last_slash(input_list):
    output_list = []
    for item in input_list:
        letters = item[0].split('/')[-1]
        output_list.append(letters)
    return output_list

# Test the function with the given inputs
input_list = [['ABCDE/FGHI/JKL/MNOPQR'], ['A/ABCDE/FGHI/JKL']]
print(get_letters_after_last_slash(input_list))
