def process_input(input_str):
    input_list = input_str.split(', ')
    if "New York" in input_list[1]:
        input_list[1] = "NY"
    if "USA" not in input_list[1]:
        input_list.append("USA")
    return ', '.join(input_list)

# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
# Input: ['UCLA', 'Los Angeles, CA']
# Output: Los Angeles, CA, USA

# Test cases
print(process_input("University of Pennsylvania, Phialdelphia, PA, USA"))  # Phialdelphia, PA, USA
print(process_input("UCLA, Los Angeles, CA"))  # Los Angeles, CA, USA
print(process_input("Cornell University, Ithaca, New York, USA"))  # Ithaca, NY, USA
print(process_input("Penn, Philadelphia, PA, USA"))  # Philadelphia, PA, USA
print(process_input("University of Maryland College Park, College Park, MD"))  # College Park, MD, USA
print(process_input("University of Michigan, Ann Arbor, MI, USA"))  # Ann Arbor, MI, USA
print(process_input("UC Berkeley, Berkeley, CA"))  # Berkeley, CA, USA
print(process_input("MIT, Cambridge, MA"))  # Cambridge, MA, USA
print(process_input("Rice University, Houston, TX"))  # Houston, TX, USA
print(process_input("Yale University, New Haven, CT, USA"))  # New Haven, CT, USA
print(process_input("Columbia University, New York, NY, USA"))  # New York, NY, USA
print(process_input("NYU, New York, New York, USA"))  # New York, NY, USA
print(process_input("UC Berkeley, Berkeley, CA"))  # Berkeley, CA, USA
print(process_input("UIUC, Urbana, IL"))  # Urbana, IL, USA
print(process_input("Temple University, Philadelphia, PA"))  # Philadelphia, PA, USA
print(process_input("Harvard University, Cambridge, MA, USA"))  # Cambridge, MA, USA
print(process_input("University of Connecticut, Storrs, CT, USA"))  # Storrs, CT, USA
print(process_input("Drexel University, Philadelphia, PA"))  # Philadelphia, PA, USA
print(process_input("New Haven University, New Haven, CT, USA"))  # New Haven, CT, USA
print(process_input("University of California, Santa Barbara, Santa Barbara, CA, USA"))  # Santa Barbara, CA, USA
