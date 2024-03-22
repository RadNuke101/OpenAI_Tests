def return_before_fifth_equal(input_list):
    result = []
    for item in input_list:
        string = item[0]
        count = 0
        for i in range(len(string) - 1, -1, -1):
            if string[i] == '=':
                count += 1
                if count == 5:
                    result.append(string[:i])
                    break
    return result

input_list = [['valentine day=1915=50==7.1=45'], ['movie blah=2blahblah, The=1914=54==7.9=17']]
output = return_before_fifth_equal(input_list)
print(output)
