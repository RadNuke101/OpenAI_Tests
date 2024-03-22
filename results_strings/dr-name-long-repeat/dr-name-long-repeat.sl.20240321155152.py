def get_doctor_name(input_str):
    input_list = input_str.split()
    first_name = input_list[0]
    return "Dr. " + first_name

# Prompt: return "Dr. " and the first input after
# Input: ['Launa Withers']
# Output: Dr. Launa

# Test cases
print(get_doctor_name('Launa Withers'))  # Dr. Launa
print(get_doctor_name('Lakenya Edison'))  # Dr. Lakenya
print(get_doctor_name('Brendan Hage'))  # Dr. Brendan
print(get_doctor_name('Bradford Lango'))  # Dr. Bradford
print(get_doctor_name('Rudolf Akiyama'))  # Dr. Rudolf
print(get_doctor_name('Lara Constable'))  # Dr. Lara
print(get_doctor_name('Madelaine Ghoston'))  # Dr. Madelaine
print(get_doctor_name('Salley Hornak'))  # Dr. Salley
print(get_doctor_name('Micha Junkin'))  # Dr. Micha
print(get_doctor_name('Teddy Bobo'))  # Dr. Teddy
