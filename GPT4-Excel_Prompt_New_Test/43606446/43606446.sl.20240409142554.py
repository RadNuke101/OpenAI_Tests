# Start time: 2024-04-09 14:49:56.325329

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of strings that follow a structured format, representing financial instrument identifiers in a trading context. Each string is composed of several components separated by dots and angle brackets. The structure can be broken down as follows:

1. **Currency Pair**: The initial part of the string (before the first dot) represents a currency pair, indicating the trade between two currencies. For example, "USD.EUR" signifies a trade involving US dollars and Euros.

2. **Exchange Information**: Following the currency pair, enclosed within angle brackets, there are three distinct pieces of information separated by commas:
   - **Exchange Name**: The first part within the brackets, such as "IDEALPRO", specifies the exchange platform or the market where the trade is taking place.
   - **Instrument Type**: The second part, "CASH", indicates the type of financial instrument involved in the trade.
   - **Settlement Currency**: The third part within the brackets represents the settlement currency, which is the currency in which the trade is settled. This can be one of the currencies involved in the trade or a third currency.

### Output Column Summary:

The output data consists of currency codes, such as "EUR", "USD", "WON", and "YEN". These codes represent the settlement currency for the trade described in the input string. The settlement currency is the final currency in which the transaction is completed or settled.

### Relationship Summary:

The relationship between the input and output data is direct and can be summarized as follows:

- The output (settlement currency) is determined by the last part of the input string, specifically the third part of the information enclosed within the angle brackets.
- The input string provides detailed information about a financial trade, including the currencies involved, the exchange platform, the type of instrument, and the settlement currency.
- The output simply extracts and presents the settlement currency from the detailed trade information provided in the input.

In essence, the output is a simplified representation focusing solely on the settlement currency aspect of the complex trade information given in the input. This relationship highlights the importance of the settlement currency in financial trades, as it is the key output or result extracted from the detailed trade specifications., and input as ['USD.EUR<IDEALPRO,CASH,EUR>'] output is EUR, input as ['USD.EUR<IDEALPRO,CASH,USD>'] output is USD, input as ['KOR.JPN<IDEALPRO,CASH,WON>'] output is WON, input as ['KOR.JPN<IDEALPRO,CASH,YEN>'] output is YEN, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(trade_info):
    """
    Extracts and returns the settlement currency from a trade information string.
    
    Parameters:
    trade_info (str): A string representing financial trade information, structured as described.
    
    Returns:
    str: The settlement currency code extracted from the trade information.
    """
    # Splitting the input string to isolate the settlement currency part
    parts = trade_info.split('<')[-1]  # This gets the part after the first '<'
    settlement_currency = parts.split(',')[-1].rstrip('>')  # Isolates the settlement currency and removes the trailing '>'
    
    return settlement_currency

# Test cases
print(generated_function('USD.EUR<IDEALPRO,CASH,EUR>'))  # Expected output: EUR
print(generated_function('USD.EUR<IDEALPRO,CASH,USD>'))  # Expected output: USD
print(generated_function('KOR.JPN<IDEALPRO,CASH,WON>'))  # Expected output: WON
print(generated_function('KOR.JPN<IDEALPRO,CASH,YEN>'))  # Expected output: YEN
print(generated_function("USD.EUR<IDEALPRO,CASH,EUR>"))  ## Output: EUR
print(generated_function("USD.EUR<IDEALPRO,CASH,USD>"))  ## Output: USD
print(generated_function("KOR.JPN<IDEALPRO,CASH,WON>"))  ## Output: WON
print(generated_function("KOR.JPN<IDEALPRO,CASH,YEN>"))  ## Output: YEN

# End time: 2024-04-09 14:50:07.333438
# Elapsed time in seconds: 11.008072069000264


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

