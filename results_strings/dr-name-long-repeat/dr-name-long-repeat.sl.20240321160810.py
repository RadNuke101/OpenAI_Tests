def get_doctor_name(input_str):
    # Prompt: return "Dr. " and the first input after
    return "Dr. " + input_str.split()[0]

# Input: 'Launa Withers'
# Output: 'Dr. Launa'
print(get_doctor_name('Launa Withers'))

# Input: 'Lakenya Edison'
# Output: 'Dr. Lakenya'
print(get_doctor_name('Lakenya Edison'))

# Input: 'Brendan Hage'
# Output: 'Dr. Brendan'
print(get_doctor_name('Brendan Hage'))

# Continue testing with other inputs...
