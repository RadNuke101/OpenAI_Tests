def remove_suffix(input_str):
    suffixes = ["Inc", "Company", "Corporation", "Enterprises"]
    
    for suffix in suffixes:
        if input_str.endswith(suffix):
            return input_str.replace(suffix, "").strip()
    
    return input_str

# Prompt: remove the words "Inc", "Company", "Corporation", or "Enterprises"
# Input: ['General Electric']
# Output: General Electric
# Input: ['General Electric Inc']
# Output: General Electric
# Input: ['General Electric Company']
# Output: General Electric
# Input: ['Microsoft']
# Output: Microsoft
# Input: ['Microsoft Corporation']
# Output: Microsoft
# Input: ['Nintendo']
# Output: Nintendo
# Input: ['Nintendo Enterprises']
# Output: Nintendo

# Test cases
print(remove_suffix('General Electric'))  # Output: General Electric
print(remove_suffix('General Electric Inc'))  # Output: General Electric
print(remove_suffix('General Electric Company'))  # Output: General Electric
print(remove_suffix('Microsoft'))  # Output: Microsoft
print(remove_suffix('Microsoft Corporation'))  # Output: Microsoft
print(remove_suffix('Nintendo'))  # Output: Nintendo
print(remove_suffix('Nintendo Enterprises'))  # Output: Nintendo
General Electric
General Electric
General Electric
Microsoft
Microsoft
Nintendo
Nintendo
