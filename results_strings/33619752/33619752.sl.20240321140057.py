# Prompt: remove the words "Inc", "Company", "Corporation", or "Enterprises"
# Input: ['General Electric'] -> Output: General Electric
# Input: ['General Electric Inc'] -> Output: General Electric
# Input: ['General Electric Company'] -> Output: General Electric
# Input: ['Microsoft'] -> Output: Microsoft
# Input: ['Microsoft Corporation'] -> Output: Microsoft
# Input: ['Nintendo'] -> Output: Nintendo
# Input: ['Nintendo Enterprises'] -> Output: Nintendo

def remove_keywords(input_str):
    keywords = ["Inc", "Company", "Corporation", "Enterprises"]
    for keyword in keywords:
        input_str = input_str.replace(keyword, "").strip()
    return input_str

# Test cases
print(remove_keywords('General Electric'))  # Output: General Electric
print(remove_keywords('General Electric Inc'))  # Output: General Electric
print(remove_keywords('General Electric Company'))  # Output: General Electric
print(remove_keywords('Microsoft'))  # Output: Microsoft
print(remove_keywords('Microsoft Corporation'))  # Output: Microsoft
print(remove_keywords('Nintendo'))  # Output: Nintendo
print(remove_keywords('Nintendo Enterprises'))  # Output: Nintendo
