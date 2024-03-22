def add_title(input_str):
    # Prompt: return "Dr. " and the first input after
    return "Dr. " + input_str.split()[0]

# Test cases
print(add_title('Launa Withers'))  # Output: Dr. Launa
print(add_title('Lakenya Edison'))  # Output: Dr. Lakenya
print(add_title('Brendan Hage'))  # Output: Dr. Brendan
print(add_title('Bradford Lango'))  # Output: Dr. Bradford
print(add_title('Rudolf Akiyama'))  # Output: Dr. Rudolf
