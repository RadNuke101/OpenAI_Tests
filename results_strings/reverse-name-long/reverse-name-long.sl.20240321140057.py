# Prompt: return second input, followed by a space, and then the first input
# Input: ['Launa', 'Withers'] Output: Withers Launa
def reverse_names(input):
    return input[1] + " " + input[0]

# Test cases
print(reverse_names(['Launa', 'Withers'])) # Output: Withers Launa
print(reverse_names(['Lakenya', 'Edison'])) # Output: Edison Lakenya
print(reverse_names(['Brendan', 'Hage'])) # Output: Hage Brendan
print(reverse_names(['Bradford', 'Lango'])) # Output: Lango Bradford
print(reverse_names(['Rudolf', 'Akiyama'])) # Output: Akiyama Rudolf
print(reverse_names(['Lara', 'Constable'])) # Output: Constable Lara
print(reverse_names(['Madelaine', 'Ghoston'])) # Output: Ghoston Madelaine
print(reverse_names(['Salley', 'Hornak'])) # Output: Hornak Salley
print(reverse_names(['Micha', 'Junkin'])) # Output: Junkin Micha
print(reverse_names(['Teddy', 'Bobo'])) # Output: Bobo Teddy
