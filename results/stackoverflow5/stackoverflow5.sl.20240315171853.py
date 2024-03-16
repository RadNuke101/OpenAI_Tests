def return_before_fifth_occurrence(input_list):
    result = []
    for item in input_list:
        string = item[0]
        count = 0
        index = len(string) - 1
        while index >= 0:
            if string[index] == '=':
                count += 1
                if count == 5:
                    result.append(string[:index])
                    break
            index -= 1
    return result

input_list = [['valentine day=1915=50==7.1=45'], ['movie blah=2blahblah, The=1914=54==7.9=17']]
output = return_before_fifth_occurrence(input_list)
print(output)
