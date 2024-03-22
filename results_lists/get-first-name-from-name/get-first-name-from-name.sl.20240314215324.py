def return_first_word(input_list):
    output = [phrase[0].split()[0] for phrase in input_list]
    return output

input_list = [['Susan Ann Chang'], ['Ayako Tanaka'], ['Bobby T. smth']]
print(return_first_word(input_list))
