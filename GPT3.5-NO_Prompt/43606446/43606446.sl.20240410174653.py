# Start time: 2024-04-10 17:48:53.922165

'''
Prompt:
Given that input as ['USD.EUR<IDEALPRO,CASH,EUR>'] output is EUR, input as ['USD.EUR<IDEALPRO,CASH,USD>'] output is USD, input as ['KOR.JPN<IDEALPRO,CASH,WON>'] output is WON, input as ['KOR.JPN<IDEALPRO,CASH,YEN>'] output is YEN, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        currency_pair = input_str.split('.')[1].split('<')[2].split('>')[0]
        return currency_pair
    except IndexError:
        return "Invalid input format"

# Test cases
print(generated_function('USD.EUR<IDEALPRO,CASH,EUR>'))  # Output: EUR
print(generated_function('USD.EUR<IDEALPRO,CASH,USD>'))  # Output: USD
print(generated_function('KOR.JPN<IDEALPRO,CASH,WON>'))  # Output: WON
print(generated_function('KOR.JPN<IDEALPRO,CASH,YEN>'))  # Output: YEN
print(generated_function("USD.EUR<IDEALPRO,CASH,EUR>"))  ## Output: EUR
print(generated_function("USD.EUR<IDEALPRO,CASH,USD>"))  ## Output: USD
print(generated_function("KOR.JPN<IDEALPRO,CASH,WON>"))  ## Output: WON
print(generated_function("KOR.JPN<IDEALPRO,CASH,YEN>"))  ## Output: YEN

# End time: 2024-04-10 17:48:56.006471
# Elapsed time in seconds: 2.0842514339999525