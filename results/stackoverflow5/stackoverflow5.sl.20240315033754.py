def return_before_fifth_equal(input_list):
    output = []
    for item in input_list:
        string = item[0]
        count = 0
        result = ''
        for char in reversed(string):
            if char == '=':
                count += 1
                if count == 5:
                    break
            result = char + result
        output.append(result)
    return output

input_list = [['valentine day=1915=50==7.1=45'], ['movie blah=2blahblah, The=1914=54==7.9=17']]
print(return_before_fifth_equal(input_list))
