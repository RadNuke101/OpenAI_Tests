# Prompt: remove "Inc" and everything after from input
# Input: ['Trucking Inc.'] -> Output: Trucking
# Input: ['New Truck Inc'] -> Output: New Truck
# Input: ['ABV Trucking Inc, LLC'] -> Output: ABV Trucking

def remove_suffix(input_str):
    if "Inc" in input_str:
        output = input_str.split("Inc")[0].strip()
    else:
        output = input_str.strip()
    return output

# Test cases
print(remove_suffix('Trucking Inc.'))  # Output: Trucking
print(remove_suffix('New Truck Inc'))  # Output: New Truck
print(remove_suffix('ABV Trucking Inc, LLC'))  # Output: ABV Trucking
