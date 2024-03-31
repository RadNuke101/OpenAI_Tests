# Start time: 2024-03-30 05:17:00.136381
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the words "Inc", "Company", "Corporation", or "Enterprises", and given input as ['General Electric'] output is General Electric, given input as ['General Electric Inc'] output is General Electric, given input as ['General Electric Company'] output is General Electric, given input as ['Microsoft'] output is Microsoft, given input as ['Microsoft Corporation'] output is Microsoft, given input as ['Nintendo'] output is Nintendo, given input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the words "Inc", "Company", "Corporation", or "Enterprises"
# Input: 'General Electric' => Output: 'General Electric'
# Input: 'General Electric Inc' => Output: 'General Electric'
# Input: 'General Electric Company' => Output: 'General Electric'
# Input: 'Microsoft' => Output: 'Microsoft'
# Input: 'Microsoft Corporation' => Output: 'Microsoft'
# Input: 'Nintendo' => Output: 'Nintendo'
# Input: 'Nintendo Enterprises' => Output: 'Nintendo'

def remove_company_suffix(input_str):
    try:
        words_to_remove = ["Inc", "Company", "Corporation", "Enterprises"]
        for word in words_to_remove:
            input_str = input_str.replace(word, "").strip()
        return input_str
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(remove_company_suffix('General Electric'))  # Output: General Electric
print(remove_company_suffix('General Electric Inc'))  # Output: General Electric
print(remove_company_suffix('General Electric Company'))  # Output: General Electric
print(remove_company_suffix('Microsoft'))  # Output: Microsoft
print(remove_company_suffix('Microsoft Corporation'))  # Output: Microsoft
print(remove_company_suffix('Nintendo'))  # Output: Nintendo
print(remove_company_suffix('Nintendo Enterprises'))  # Output: Nintendo

# End time: 2024-03-30 05:17:06.500047
# Elapsed time in seconds: 6.363669927999581