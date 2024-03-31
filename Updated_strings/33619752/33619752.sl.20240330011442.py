# Start time: 2024-03-30 01:25:48.156308
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the words "Inc", "Company", "Corporation", or "Enterprises", and given input as ['General Electric'] output is General Electric, given input as ['General Electric Inc'] output is General Electric, given input as ['General Electric Company'] output is General Electric, given input as ['Microsoft'] output is Microsoft, given input as ['Microsoft Corporation'] output is Microsoft, given input as ['Nintendo'] output is Nintendo, given input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the words "Inc", "Company", "Corporation", or "Enterprises"
# Input: 'General Electric' => Output: 'General Electric'
# Input: 'General Electric Inc' => Output: 'General Electric'
# Input: 'General Electric Company' => Output: 'General Electric'
# Input: 'Microsoft' => Output: 'Microsoft'
# Input: 'Microsoft Corporation' => Output: 'Microsoft'
# Input: 'Nintendo' => Output: 'Nintendo'
# Input: 'Nintendo Enterprises' => Output: 'Nintendo'

def remove_words(input_str):
    try:
        input_str = input_str.replace(" Inc", "").replace(" Company", "").replace(" Corporation", "").replace(" Enterprises", "")
        return input_str
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(remove_words('General Electric'))  # Output: General Electric
print(remove_words('General Electric Inc'))  # Output: General Electric
print(remove_words('General Electric Company'))  # Output: General Electric
print(remove_words('Microsoft'))  # Output: Microsoft
print(remove_words('Microsoft Corporation'))  # Output: Microsoft
print(remove_words('Nintendo'))  # Output: Nintendo
print(remove_words('Nintendo Enterprises'))  # Output: Nintendo

# End time: 2024-03-30 01:25:54.391355
# Elapsed time in seconds: 6.234934276000786