def remove_company_name(input_str):
    company_names = ["Inc", "Company", "Corporation", "Enterprises"]
    
    for name in company_names:
        input_str = input_str.replace(name, "").strip()
    
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
print(remove_company_name('General Electric'))  # Output: General Electric
print(remove_company_name('General Electric Inc'))  # Output: General Electric
print(remove_company_name('General Electric Company'))  # Output: General Electric
print(remove_company_name('Microsoft'))  # Output: Microsoft
print(remove_company_name('Microsoft Corporation'))  # Output: Microsoft
print(remove_company_name('Nintendo'))  # Output: Nintendo
print(remove_company_name('Nintendo Enterprises'))  # Output: Nintendo
