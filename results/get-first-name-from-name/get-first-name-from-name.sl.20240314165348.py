def get_first_word(input_list):
    return [phrase[0].split()[0] for phrase in input_list]

input_list = [['Susan Ann Chang'], ['Ayako Tanaka'], ['Bobby T. smth']]
output = get_first_word(input_list)
print(output)
