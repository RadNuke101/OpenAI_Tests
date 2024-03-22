# Prompt: remove "Inc" and everything after from input
# Input: ['Trucking Inc.'] Output: Trucking
# Input: ['New Truck Inc'] Output: New Truck
# Input: ['ABV Trucking Inc, LLC'] Output: ABV Trucking

def remove_inc(input_str):
    result = input_str.replace(" Inc", "").split(',')[0]
    return result

# Test cases
print(remove_inc('Trucking Inc.'))  # Output: Trucking
print(remove_inc('New Truck Inc'))  # Output: New Truck
print(remove_inc('ABV Trucking Inc, LLC'))  # Output: ABV Trucking
