def get_doctor_name(input_str):
    # Prompt: return "Dr. " and the first input after
    return "Dr. " + input_str.split()[0]

# Test cases
print(get_doctor_name('Launa Withers'))  # Output: Dr. Launa
print(get_doctor_name('Lakenya Edison'))  # Output: Dr. Lakenya
print(get_doctor_name('Brendan Hage'))  # Output: Dr. Brendan
print(get_doctor_name('Bradford Lango'))  # Output: Dr. Bradford
print(get_doctor_name('Rudolf Akiyama'))  # Output: Dr. Rudolf
print(get_doctor_name('Lara Constable'))  # Output: Dr. Lara
print(get_doctor_name('Madelaine Ghoston'))  # Output: Dr. Madelaine
print(get_doctor_name('Salley Hornak'))  # Output: Dr. Salley
print(get_doctor_name('Micha Junkin'))  # Output: Dr. Micha
print(get_doctor_name('Teddy Bobo'))  # Output: Dr. Teddy
