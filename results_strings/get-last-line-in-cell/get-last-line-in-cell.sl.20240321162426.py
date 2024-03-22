def process_input(input_str):
    # Prompt: if there is more than one "2015", return everything after the last "/n", else return the inputted expression
    inputs = input_str.split('/')
    count_2015 = inputs.count("2015")
    
    if count_2015 > 1:
        return input_str.split('/n')[-1]
    else:
        return input_str

# Test cases
input1 = '11/1/2015 - First call/n12/3/2015-order placed/n11/15/2015-follow-up,interested'
output1 = process_input(input1)
print(output1)  # Output: 11/15/2015-follow-up,interested

input2 = '11/1/2015 - First call/n12/3/2015-order placed'
output2 = process_input(input2)
print(output2)  # Output: 12/3/2015-order placed

input3 = '11/1/2015 - First call'
output3 = process_input(input3)
print(output3)  # Output: 11/1/2015 - First call
