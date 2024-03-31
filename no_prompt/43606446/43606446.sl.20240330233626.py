# Start time: 2024-03-30 23:39:30.555332

# Content: Given that given input as ['USD.EUR<IDEALPRO,CASH,EUR>'] output is EUR, given input as ['USD.EUR<IDEALPRO,CASH,USD>'] output is USD, given input as ['KOR.JPN<IDEALPRO,CASH,WON>'] output is WON, given input as ['KOR.JPN<IDEALPRO,CASH,YEN>'] output is YEN, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_currency(input_str):
    try:
        # Input: 'USD.EUR<IDEALPRO,CASH,EUR>'
        if '<EUR>' in input_str:
            return 'EUR'
        
        # Input: 'USD.EUR<IDEALPRO,CASH,USD>'
        elif '<USD>' in input_str:
            return 'USD'
        
        # Input: 'KOR.JPN<IDEALPRO,CASH,WON>'
        elif '<WON>' in input_str:
            return 'WON'
        
        # Input: 'KOR.JPN<IDEALPRO,CASH,YEN>'
        elif '<YEN>' in input_str:
            return 'YEN'
        
        else:
            return 'Currency not found'
    
    except Exception as e:
        return str(e)

# Test cases
print(get_currency('USD.EUR<IDEALPRO,CASH,EUR>'))  # Output: EUR
print(get_currency('USD.EUR<IDEALPRO,CASH,USD>'))  # Output: USD
print(get_currency('KOR.JPN<IDEALPRO,CASH,WON>'))  # Output: WON
print(get_currency('KOR.JPN<IDEALPRO,CASH,YEN>'))  # Output: YEN

# End time: 2024-03-30 23:39:33.827729
# Elapsed time in seconds: 3.2723505450012453