def first_word(input_list):
    return [phrase[0].split()[0] for phrase in input_list]

input_list = [['Susan Ann Chang'], ['Ayako Tanaka'], ['Bobby T. smth']]
output = first_word(input_list)
print(output)
