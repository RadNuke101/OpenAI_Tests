def return_before_fifth_equal(input_list):
    result = []
    for item in input_list:
        string = item[0]
        count = 0
        index = len(string) - 1
        while count < 5 and index >= 0:
            if string[index] == '=':
                count += 1
            index -= 1
        result.append(string[:index + 2])
    return result

input_list = [['valentine day=1915=50==7.1=45'], ['movie blah=2blahblah, The=1914=54==7.9=17']]
output = return_before_fifth_equal(input_list)
print(output)
