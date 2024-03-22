def process_input(input_str):
    if input_str.count("2015") > 1:
        return input_str.split("/n")[-1]
    else:
        return input_str

# Prompt: if there is more than one "2015", return everything after the last "/n", else return the inputted expression
# Input: ['11/1/2015 - First call/n12/3/2015-order placed/n11/15/2015-follow-up,interested']
# Output: '11/15/2015-follow-up,interested'
# Input: ['11/1/2015 - First call/n12/3/2015-order placed']
# Output: '12/3/2015-order placed'
# Input: ['11/1/2015 - First call']
# Output: '11/1/2015 - First call'

# Test cases
print(process_input('11/1/2015 - First call/n12/3/2015-order placed/n11/15/2015-follow-up,interested'))
print(process_input('11/1/2015 - First call/n12/3/2015-order placed'))
print(process_input('11/1/2015 - First call'))
11/15/2015-follow-up,interested
12/3/2015-order placed
11/1/2015 - First call
