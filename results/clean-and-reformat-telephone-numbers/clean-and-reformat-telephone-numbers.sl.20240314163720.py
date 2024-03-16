def clean_phone_numbers(phone_numbers):
    cleaned_numbers = []
    for number in phone_numbers:
        cleaned_number = ''.join(char for char in number[0] if char.isdigit())
        cleaned_numbers.append(cleaned_number)
    return cleaned_numbers

input_numbers = [['801-456-8765'], ['<978> 654-0299'], ['978.654.0299']]
output_numbers = clean_phone_numbers(input_numbers)
print(output_numbers)
