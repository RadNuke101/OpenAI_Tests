# Start time: 2024-03-30 22:17:33.534969

# Content: Given that given input as ['USD.EUR<IDEALPRO,CASH,EUR>'] output is EUR, given input as ['USD.EUR<IDEALPRO,CASH,USD>'] output is USD, given input as ['KOR.JPN<IDEALPRO,CASH,WON>'] output is WON, given input as ['KOR.JPN<IDEALPRO,CASH,YEN>'] output is YEN, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'USD.EUR<IDEALPRO,CASH,EUR>', output: 'EUR'
# input: 'USD.EUR<IDEALPRO,CASH,USD>', output: 'USD'
# input: 'KOR.JPN<IDEALPRO,CASH,WON>', output: 'WON'
# input: 'KOR.JPN<IDEALPRO,CASH,YEN>', output: 'YEN'

def extract_currency(input_str):
    try:
        # Split the input string by '<' and '>'
        currency = input_str.split('<')[1].split('>')[0]
        return currency
    except IndexError:
        return "Invalid input format"

# Test cases
print(extract_currency('USD.EUR<IDEALPRO,CASH,EUR>'))  # Output: EUR
print(extract_currency('USD.EUR<IDEALPRO,CASH,USD>'))  # Output: USD
print(extract_currency('KOR.JPN<IDEALPRO,CASH,WON>'))  # Output: WON
print(extract_currency('KOR.JPN<IDEALPRO,CASH,YEN>'))  # Output: YEN

# End time: 2024-03-30 22:17:36.005863
# Elapsed time in seconds: 2.470822610999676