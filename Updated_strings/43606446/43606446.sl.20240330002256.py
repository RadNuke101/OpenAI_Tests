# Start time: 2024-03-30 00:26:29.143440
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the three capitalized letters before the ">" in the expression, and given input as ['USD.EUR<IDEALPRO,CASH,EUR>'] output is EUR, given input as ['USD.EUR<IDEALPRO,CASH,USD>'] output is USD, given input as ['KOR.JPN<IDEALPRO,CASH,WON>'] output is WON, given input as ['KOR.JPN<IDEALPRO,CASH,YEN>'] output is YEN, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the three capitalized letters before the ">" in the expression
# Input: ['USD.EUR<IDEALPRO,CASH,EUR>'], Output: EUR
# Input: ['USD.EUR<IDEALPRO,CASH,USD>'], Output: USD
# Input: ['KOR.JPN<IDEALPRO,CASH,WON>'], Output: WON
# Input: ['KOR.JPN<IDEALPRO,CASH,YEN>'], Output: YEN

def extract_currency(input_str):
    try:
        # Extracting the substring before the ">" symbol
        currency = input_str[0].split("<")[1].split(",")[-1]
        return currency.upper()
    except:
        return "Invalid input"

# Test cases
print(extract_currency(['USD.EUR<IDEALPRO,CASH,EUR>']))  # Output: EUR
print(extract_currency(['USD.EUR<IDEALPRO,CASH,USD>']))  # Output: USD
print(extract_currency(['KOR.JPN<IDEALPRO,CASH,WON>']))  # Output: WON
print(extract_currency(['KOR.JPN<IDEALPRO,CASH,YEN>']))  # Output: YEN

# End time: 2024-03-30 00:26:32.345631
# Elapsed time in seconds: 3.201982890999716