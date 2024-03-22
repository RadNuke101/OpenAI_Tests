def return_before_fifth_equal(input_list):
    output_list = []
    for item in input_list:
        text = item[0]
        count = 0
        for i in range(len(text)-1, -1, -1):
            if text[i] == '=':
                count += 1
                if count == 5:
                    output_list.append(text[:i])
                    break
    return output_list

input_list = [['valentine day=1915=50==7.1=45'], ['movie blah=2blahblah, The=1914=54==7.9=17']]
print(return_before_fifth_equal(input_list))
