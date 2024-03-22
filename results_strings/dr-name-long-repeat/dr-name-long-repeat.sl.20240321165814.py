# Prompt: return "Dr. " and the first input after
# Given input as ['Launa Withers'] output is Dr. Launa

def add_title(input_str):
    name = input_str.split()[0]
    return "Dr. " + name

# Test cases
print(add_title('Launa Withers')) # Output: Dr. Launa
print(add_title('Lakenya Edison')) # Output: Dr. Lakenya
print(add_title('Brendan Hage')) # Output: Dr. Brendan
print(add_title('Bradford Lango')) # Output: Dr. Bradford
print(add_title('Rudolf Akiyama')) # Output: Dr. Rudolf
print(add_title('Lara Constable')) # Output: Dr. Lara
print(add_title('Madelaine Ghoston')) # Output: Dr. Madelaine
print(add_title('Salley Hornak')) # Output: Dr. Salley
print(add_title('Micha Junkin')) # Output: Dr. Micha
print(add_title('Teddy Bobo')) # Output: Dr. Teddy
print(add_title('Coralee Scalia')) # Output: Dr. Coralee
print(add_title('Jeff Quashie')) # Output: Dr. Jeff
print(add_title('Vena Babiarz')) # Output: Dr. Vena
print(add_title('Karrie Lain')) # Output: Dr. Karrie
print(add_title('Tobias Dermody')) # Output: Dr. Tobias
print(add_title('Celsa Hopkins')) # Output: Dr. Celsa
print(add_title('Kimberley Halpern')) # Output: Dr. Kimberley
print(add_title('Phillip Rowden')) # Output: Dr. Phillip
print(add_title('Elias Neil')) # Output: Dr. Elias
print(add_title('Lashanda Cortes')) # Output: Dr. Lashanda
