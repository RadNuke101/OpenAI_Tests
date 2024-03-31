# Start time: 2024-03-30 22:14:12.013984

# Content: Given that given input as ['Launa Withers'] output is Dr. Launa, given input as ['Lakenya Edison'] output is Dr. Lakenya, given input as ['Brendan Hage'] output is Dr. Brendan, given input as ['Bradford Lango'] output is Dr. Bradford, given input as ['Rudolf Akiyama'] output is Dr. Rudolf, given input as ['Lara Constable'] output is Dr. Lara, given input as ['Madelaine Ghoston'] output is Dr. Madelaine, given input as ['Salley Hornak'] output is Dr. Salley, given input as ['Micha Junkin'] output is Dr. Micha, given input as ['Teddy Bobo'] output is Dr. Teddy, given input as ['Coralee Scalia'] output is Dr. Coralee, given input as ['Jeff Quashie'] output is Dr. Jeff, given input as ['Vena Babiarz'] output is Dr. Vena, given input as ['Karrie Lain'] output is Dr. Karrie, given input as ['Tobias Dermody'] output is Dr. Tobias, given input as ['Celsa Hopkins'] output is Dr. Celsa, given input as ['Kimberley Halpern'] output is Dr. Kimberley, given input as ['Phillip Rowden'] output is Dr. Phillip, given input as ['Elias Neil'] output is Dr. Elias, given input as ['Lashanda Cortes'] output is Dr. Lashanda, given input as ['Mackenzie Spell'] output is Dr. Mackenzie, given input as ['Kathlyn Eccleston'] output is Dr. Kathlyn, given input as ['Georgina Brescia'] output is Dr. Georgina, given input as ['Beata Miah'] output is Dr. Beata, given input as ['Desiree Seamons'] output is Dr. Desiree, given input as ['Jeanice Soderstrom'] output is Dr. Jeanice, given input as ['Mariel Jurgens'] output is Dr. Mariel, given input as ['Alida Bogle'] output is Dr. Alida, given input as ['Jacqualine Olague'] output is Dr. Jacqualine, given input as ['Joaquin Clasen'] output is Dr. Joaquin, given input as ['Samuel Richert'] output is Dr. Samuel, given input as ['Malissa Marcus'] output is Dr. Malissa, given input as ['Alaina Partida'] output is Dr. Alaina, given input as ['Trinidad Mulloy'] output is Dr. Trinidad, given input as ['Carlene Garrard'] output is Dr. Carlene, given input as ['Melodi Chism'] output is Dr. Melodi, given input as ['Bess Chilcott'] output is Dr. Bess, given input as ['Chong Aylward'] output is Dr. Chong, given input as ['Jani Ramthun'] output is Dr. Jani, given input as ['Jacquiline Heintz'] output is Dr. Jacquiline, given input as ['Hayley Marquess'] output is Dr. Hayley, given input as ['Andria Spagnoli'] output is Dr. Andria, given input as ['Irwin Covelli'] output is Dr. Irwin, given input as ['Gertude Montiel'] output is Dr. Gertude, given input as ['Stefany Reily'] output is Dr. Stefany, given input as ['Rae Mcgaughey'] output is Dr. Rae, given input as ['Cruz Latimore'] output is Dr. Cruz, given input as ['Maryann Casler'] output is Dr. Maryann, given input as ['Annalisa Gregori'] output is Dr. Annalisa, given input as ['Jenee Pannell'] output is Dr. Jenee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def generate_doctor_name(input_name):
    try:
        # Input: 'Launa Withers' => Output: 'Dr. Launa'
        first_name = input_name.split()[0]
        doctor_name = 'Dr. ' + first_name
        return doctor_name
    except Exception as e:
        print(f"Error: {e}")

# Test cases
print(generate_doctor_name('Launa Withers'))  # Output: Dr. Launa
print(generate_doctor_name('Lakenya Edison'))  # Output: Dr. Lakenya
print(generate_doctor_name('Brendan Hage'))  # Output: Dr. Brendan
print(generate_doctor_name('Bradford Lango'))  # Output: Dr. Bradford
print(generate_doctor_name('Rudolf Akiyama'))  # Output: Dr. Rudolf
print(generate_doctor_name('Lara Constable'))  # Output: Dr. Lara
print(generate_doctor_name('Madelaine Ghoston'))  # Output: Dr. Madelaine
print(generate_doctor_name('Salley Hornak'))  # Output: Dr. Salley
print(generate_doctor_name('Micha Junkin'))  # Output: Dr. Micha
print(generate_doctor_name('Teddy Bobo'))  # Output: Dr. Teddy
print(generate_doctor_name('Coralee Scalia'))  # Output: Dr. Coralee
print(generate_doctor_name('Jeff Quashie'))  # Output: Dr. Jeff
print(generate_doctor_name('Vena Babiarz'))  # Output: Dr. Vena
print(generate_doctor_name('Karrie Lain'))  # Output: Dr. Karrie
print(generate_doctor_name('Tobias Dermody'))  # Output: Dr. Tobias
print(generate_doctor_name('Celsa Hopkins'))  # Output: Dr. Celsa
print(generate_doctor_name('Kimberley Halpern'))  # Output: Dr. Kimberley
print(generate_doctor_name('Phillip Rowden'))  # Output: Dr. Phillip
print(generate_doctor_name('Elias Neil'))  # Output: Dr. Elias
print(generate_doctor_name('Lashanda Cortes'))  # Output: Dr. Lashanda
print(generate_doctor_name('Mackenzie Spell'))  # Output: Dr. Mackenzie
print(generate_doctor_name('Kathlyn Eccleston'))  # Output: Dr. Kathlyn
print(generate_doctor_name('Georgina Brescia'))  # Output: Dr. Georgina
print(generate_doctor_name('Beata Miah'))  # Output: Dr. Beata
print(generate_doctor_name('Desiree Seamons'))  # Output: Dr. Desiree
print(generate_doctor_name('Jeanice Soderstrom'))  # Output: Dr. Jeanice
print(generate_doctor_name('Mariel Jurgens'))  # Output: Dr. Mariel
print(generate_doctor_name('Alida Bogle'))  # Output: Dr. Alida
print(generate_doctor_name('Jacqualine Olague'))  # Output: Dr. Jacqualine
print(generate_doctor_name('Joaquin Clasen'))  # Output: Dr. Joaquin
print(generate_doctor_name('Samuel Richert'))  # Output: Dr. Samuel
print(generate_doctor_name('Malissa Marcus'))  # Output: Dr. Malissa
print(generate_doctor_name('Alaina Partida'))  # Output: Dr. Alaina
print(generate_doctor_name('Trinidad Mulloy'))  # Output: Dr. Trinidad
print(generate_doctor_name('Carlene Garrard'))  # Output: Dr. Carlene
print(generate_doctor_name('Melodi Chism'))  # Output: Dr. Melodi
print(generate_doctor_name('Bess Chilcott'))  # Output: Dr. Bess
print(generate_doctor_name('Chong Aylward'))  # Output: Dr. Chong
print(generate_doctor_name('Jani Ramthun'))  # Output: Dr. Jani
print(generate_doctor_name('Jacquiline Heintz'))  # Output: Dr. Jacquiline
print(generate_doctor_name('Hayley Marquess'))  # Output: Dr. Hayley
print(generate_doctor_name('Andria Spagnoli'))  # Output: Dr. Andria
print(generate_doctor_name('Irwin Covelli'))  # Output: Dr. Irwin
print(generate_doctor_name('Gertude Montiel'))  # Output: Dr. Gertude
print(generate_doctor_name('Stefany Reily'))  # Output: Dr. Stefany
print(generate_doctor_name('Rae Mcgaughey'))  # Output: Dr. Rae
print(generate_doctor_name('Cruz Latimore'))  # Output: Dr. Cruz
print(generate_doctor_name('Maryann Casler'))  # Output: Dr. Maryann
print(generate_doctor_name('Annalisa Gregori'))  # Output: Dr. Annalisa
print(generate_doctor_name('Jenee Pannell'))  # Output: Dr. Jenee

# End time: 2024-03-30 22:14:29.448039
# Elapsed time in seconds: 17.433599460999176