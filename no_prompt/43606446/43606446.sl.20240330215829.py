# Start time: 2024-03-30 22:01:27.718856

# Content: Given that given input as ['USD.EUR<IDEALPRO,CASH,EUR>'] output is EUR, given input as ['USD.EUR<IDEALPRO,CASH,USD>'] output is USD, given input as ['KOR.JPN<IDEALPRO,CASH,WON>'] output is WON, given input as ['KOR.JPN<IDEALPRO,CASH,YEN>'] output is YEN, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_currency(input_str):
    try:
        # Input: 'USD.EUR<IDEALPRO,CASH,EUR>'
        if '<' in input_str and '>' in input_str:
            currency = input_str.split('<')[1].split('>')[0].split(',')[-1]
            return currency
        else:
            raise ValueError("Invalid input format")
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test cases
print(get_currency('USD.EUR<IDEALPRO,CASH,EUR>'))  # Output: EUR
print(get_currency('USD.EUR<IDEALPRO,CASH,USD>'))  # Output: USD
print(get_currency('KOR.JPN<IDEALPRO,CASH,WON>'))  # Output: WON
print(get_currency('KOR.JPN<IDEALPRO,CASH,YEN>'))  # Output: YEN

# End time: 2024-03-30 22:01:30.454666
# Elapsed time in seconds: 2.735722524999801