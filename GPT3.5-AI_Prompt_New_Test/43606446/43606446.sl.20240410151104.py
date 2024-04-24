# Start time: 2024-04-10 15:15:06.088039

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of currency pairs with different exchange options (IDEALPRO, CASH) and currency options (EUR, USD, WON, YEN).
- The currency pairs include USD.EUR, KOR.JPN.
- The exchange options include IDEALPRO and CASH.
- The currency options include EUR, USD, WON, YEN.

Summary for Output Column Data:
- The output column data consists of currency options (EUR, USD, WON, YEN).
- The output column represents the currency that is being exchanged to in each input.

Relationship between Input and Output:
- The input column data specifies the currency pair and exchange options, while the output column specifies the currency that is being exchanged to.
- The output currency is determined by the second currency in the currency pair in the input column.
- The relationship between the input and output is that the output currency is the currency that is being exchanged to based on the input currency pair and exchange options., and input as ['USD.EUR<IDEALPRO,CASH,EUR>'] output is EUR, input as ['USD.EUR<IDEALPRO,CASH,USD>'] output is USD, input as ['KOR.JPN<IDEALPRO,CASH,WON>'] output is WON, input as ['KOR.JPN<IDEALPRO,CASH,YEN>'] output is YEN, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string to extract currency pair and exchange option
    input_list = input_str.split('<')
    currency_pair = input_list[0]
    exchange_option = input_list[1].split(',')[0]
    
    # Determine the output currency based on the currency pair
    if currency_pair.endswith('.EUR'):
        return 'EUR'
    elif currency_pair.endswith('.USD'):
        return 'USD'
    elif currency_pair.endswith('.WON'):
        return 'WON'
    elif currency_pair.endswith('.YEN'):
        return 'YEN'

# Test cases
print(generated_function('USD.EUR<IDEALPRO,CASH,EUR>'))  # Output: EUR
print(generated_function('USD.EUR<IDEALPRO,CASH,USD>'))  # Output: USD
print(generated_function('KOR.JPN<IDEALPRO,CASH,WON>'))  # Output: WON
print(generated_function('KOR.JPN<IDEALPRO,CASH,YEN>'))  # Output: YEN
print(generated_function("USD.EUR<IDEALPRO,CASH,EUR>"))  ## Output: EUR
print(generated_function("USD.EUR<IDEALPRO,CASH,USD>"))  ## Output: USD
print(generated_function("KOR.JPN<IDEALPRO,CASH,WON>"))  ## Output: WON
print(generated_function("KOR.JPN<IDEALPRO,CASH,YEN>"))  ## Output: YEN

# End time: 2024-04-10 15:15:09.284711
# Elapsed time in seconds: 3.19660186100009


# APPEND TEST SCRIPTS...
print(generated_function("USD.EUR<IDEALPRO,CASH,EUR>"))  ## Output: EUR
print(generated_function("USD.EUR<IDEALPRO,CASH,USD>"))  ## Output: USD
print(generated_function("KOR.JPN<IDEALPRO,CASH,WON>"))  ## Output: WON
print(generated_function("KOR.JPN<IDEALPRO,CASH,YEN>"))  ## Output: YEN


print(generated_function("USD.JPN<IDEALPRO,CASH,USD>"))  ### Output: USD
print(generated_function("KOR.EUR<IDEALPRO,CASH,WON>"))  ### Output: WON
print(generated_function("KOR.EUR<IDEALPRO,CASH,EUR>"))  ### Output: EUR
print(generated_function("USD.JPN<IDEALPRO,CASH,YEN>"))  ### Output: YEN

# TEST SCRIPTS APPENDED!

