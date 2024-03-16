def return_letters_after_last_slash(input_list):
    output_list = []
    for item in input_list:
        last_slash_index = item[0].rfind('/')
        output_list.append(item[0][last_slash_index+1:])
    return output_list

# Test the function with the provided input
input_list = [['ABCDE/FGHI/JKL/MNOPQR'], ['A/ABCDE/FGHI/JKL']]
print(return_letters_after_last_slash(input_list))
