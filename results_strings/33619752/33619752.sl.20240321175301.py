# Prompt: remove the words "Inc", "Company", "Corporation", or "Enterprises"
# Input: ['General Electric'] Output: General Electric
# Input: ['General Electric Inc'] Output: General Electric
# Input: ['General Electric Company'] Output: General Electric
# Input: ['Microsoft'] Output: Microsoft
# Input: ['Microsoft Corporation'] Output: Microsoft
# Input: ['Nintendo'] Output: Nintendo
# Input: ['Nintendo Enterprises'] Output: Nintendo

def remove_words(input_str):
    words_to_remove = ["Inc", "Company", "Corporation", "Enterprises"]
    
    for word in words_to_remove:
        if word in input_str:
            input_str = input_str.replace(word, "").strip()
    
    return input_str

# Test cases
print(remove_words('General Electric'))  # Output: General Electric
print(remove_words('General Electric Inc'))  # Output: General Electric
print(remove_words('General Electric Company'))  # Output: General Electric
print(remove_words('Microsoft'))  # Output: Microsoft
print(remove_words('Microsoft Corporation'))  # Output: Microsoft
print(remove_words('Nintendo'))  # Output: Nintendo
print(remove_words('Nintendo Enterprises'))  # Output: Nintendo
