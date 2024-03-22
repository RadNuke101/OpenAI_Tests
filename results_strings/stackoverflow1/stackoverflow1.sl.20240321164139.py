# Prompt: remove "Inc" and everything after from input
# Input: ['Trucking Inc.'] Output: Trucking
# Input: ['New Truck Inc'] Output: New Truck
# Input: ['ABV Trucking Inc, LLC'] Output: ABV Trucking

def remove_inc(input_str):
    # Remove "Inc" and everything after from the input string
    output_str = input_str.split(' Inc')[0]
    return output_str

# Test cases
print(remove_inc('Trucking Inc.'))  # Output: Trucking
print(remove_inc('New Truck Inc'))  # Output: New Truck
print(remove_inc('ABV Trucking Inc, LLC'))  # Output: ABV Trucking
Trucking
New Truck
ABV Trucking
