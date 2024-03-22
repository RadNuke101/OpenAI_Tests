# Prompt: return "Dr. " and the first input after
# Given input as ['Launa Withers'] output is Dr. Launa
# Given input as ['Lakenya Edison'] output is Dr. Lakenya
# Given input as ['Brendan Hage'] output is Dr. Brendan
# ...

def generate_doctor_name(input_str):
    input_list = input_str.split()
    return "Dr. " + input_list[0]

# Test cases
print(generate_doctor_name("Launa Withers"))  # Output: Dr. Launa
print(generate_doctor_name("Lakenya Edison"))  # Output: Dr. Lakenya
print(generate_doctor_name("Brendan Hage"))  # Output: Dr. Brendan
