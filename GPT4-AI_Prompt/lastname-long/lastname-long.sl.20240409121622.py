# Start time: 2024-04-09 13:28:20.764678

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing full names of individuals. Each entry in this column is a combination of a first name and a last name, separated by a space. The names appear to be diverse, indicating no specific cultural, geographical, or gender bias. The dataset includes a wide variety of names, suggesting a broad representation of individuals. Each name is unique, with no repetitions observed in the dataset provided.

### Output Column Summary:

The output data extracts and presents the last name from each full name provided in the input column. This transformation isolates the second part of each full name, effectively separating the last names from the first names. The output retains the diversity and uniqueness of the names, now focusing solely on the family names or surnames. Like the input, there is no apparent bias in terms of origin or gender, maintaining a broad representation.

### Relationship Summary:

The relationship between the input and output data is straightforward: the output is derived directly from the input by isolating and extracting the last name from each full name. This process involves identifying the space that separates the first name from the last name in the input and then selecting the portion of the string that follows this space. The transformation does not alter the original last names in any way, ensuring that the output is a faithful representation of the second part of each full name provided in the input. This method demonstrates a clear, systematic approach to separating individual components of full names, specifically focusing on extracting surnames for the output., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, input as ['Launa Withers'] output is Withers, input as ['Lakenya Edison'] output is Edison, input as ['Brendan Hage'] output is Hage, input as ['Bradford Lango'] output is Lango, input as ['Rudolf Akiyama'] output is Akiyama, input as ['Lara Constable'] output is Constable, input as ['Madelaine Ghoston'] output is Ghoston, input as ['Salley Hornak'] output is Hornak, input as ['Micha Junkin'] output is Junkin, input as ['Teddy Bobo'] output is Bobo, input as ['Coralee Scalia'] output is Scalia, input as ['Jeff Quashie'] output is Quashie, input as ['Vena Babiarz'] output is Babiarz, input as ['Karrie Lain'] output is Lain, input as ['Tobias Dermody'] output is Dermody, input as ['Celsa Hopkins'] output is Hopkins, input as ['Kimberley Halpern'] output is Halpern, input as ['Phillip Rowden'] output is Rowden, input as ['Elias Neil'] output is Neil, input as ['Lashanda Cortes'] output is Cortes, input as ['Mackenzie Spell'] output is Spell, input as ['Kathlyn Eccleston'] output is Eccleston, input as ['Georgina Brescia'] output is Brescia, input as ['Beata Miah'] output is Miah, input as ['Desiree Seamons'] output is Seamons, input as ['Jeanice Soderstrom'] output is Soderstrom, input as ['Mariel Jurgens'] output is Jurgens, input as ['Alida Bogle'] output is Bogle, input as ['Jacqualine Olague'] output is Olague, input as ['Joaquin Clasen'] output is Clasen, input as ['Samuel Richert'] output is Richert, input as ['Malissa Marcus'] output is Marcus, input as ['Alaina Partida'] output is Partida, input as ['Trinidad Mulloy'] output is Mulloy, input as ['Carlene Garrard'] output is Garrard, input as ['Melodi Chism'] output is Chism, input as ['Bess Chilcott'] output is Chilcott, input as ['Chong Aylward'] output is Aylward, input as ['Jani Ramthun'] output is Ramthun, input as ['Jacquiline Heintz'] output is Heintz, input as ['Hayley Marquess'] output is Marquess, input as ['Andria Spagnoli'] output is Spagnoli, input as ['Irwin Covelli'] output is Covelli, input as ['Gertude Montiel'] output is Montiel, input as ['Stefany Reily'] output is Reily, input as ['Rae Mcgaughey'] output is Mcgaughey, input as ['Cruz Latimore'] output is Latimore, input as ['Maryann Casler'] output is Casler, input as ['Annalisa Gregori'] output is Gregori, input as ['Jenee Pannell'] output is Pannell, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a full name.
    
    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts and return the last part (assumed to be the last name)
    return full_name.split(" ")[-1]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function('Launa Withers'))  # Expected output: Withers
print(generated_function('Lakenya Edison'))  # Expected output: Edison
print(generated_function('Brendan Hage'))  # Expected output: Hage
print(generated_function('Bradford Lango'))  # Expected output: Lango
print(generated_function('Rudolf Akiyama'))  # Expected output: Akiyama
print(generated_function('Lara Constable'))  # Expected output: Constable
# Additional test cases can be added following the same pattern
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko
print(generated_function("Launa Withers"))  ## Output: Withers
print(generated_function("Lakenya Edison"))  ## Output: Edison
print(generated_function("Brendan Hage"))  ## Output: Hage
print(generated_function("Bradford Lango"))  ## Output: Lango
print(generated_function("Rudolf Akiyama"))  ## Output: Akiyama
print(generated_function("Lara Constable"))  ## Output: Constable
print(generated_function("Madelaine Ghoston"))  ## Output: Ghoston
print(generated_function("Salley Hornak"))  ## Output: Hornak
print(generated_function("Micha Junkin"))  ## Output: Junkin
print(generated_function("Teddy Bobo"))  ## Output: Bobo
print(generated_function("Coralee Scalia"))  ## Output: Scalia
print(generated_function("Jeff Quashie"))  ## Output: Quashie
print(generated_function("Vena Babiarz"))  ## Output: Babiarz
print(generated_function("Karrie Lain"))  ## Output: Lain
print(generated_function("Tobias Dermody"))  ## Output: Dermody
print(generated_function("Celsa Hopkins"))  ## Output: Hopkins
print(generated_function("Kimberley Halpern"))  ## Output: Halpern
print(generated_function("Phillip Rowden"))  ## Output: Rowden
print(generated_function("Elias Neil"))  ## Output: Neil
print(generated_function("Lashanda Cortes"))  ## Output: Cortes
print(generated_function("Mackenzie Spell"))  ## Output: Spell
print(generated_function("Kathlyn Eccleston"))  ## Output: Eccleston
print(generated_function("Georgina Brescia"))  ## Output: Brescia
print(generated_function("Beata Miah"))  ## Output: Miah
print(generated_function("Desiree Seamons"))  ## Output: Seamons
print(generated_function("Jeanice Soderstrom"))  ## Output: Soderstrom
print(generated_function("Mariel Jurgens"))  ## Output: Jurgens
print(generated_function("Alida Bogle"))  ## Output: Bogle
print(generated_function("Jacqualine Olague"))  ## Output: Olague
print(generated_function("Joaquin Clasen"))  ## Output: Clasen
print(generated_function("Samuel Richert"))  ## Output: Richert
print(generated_function("Malissa Marcus"))  ## Output: Marcus
print(generated_function("Alaina Partida"))  ## Output: Partida
print(generated_function("Trinidad Mulloy"))  ## Output: Mulloy
print(generated_function("Carlene Garrard"))  ## Output: Garrard
print(generated_function("Melodi Chism"))  ## Output: Chism
print(generated_function("Bess Chilcott"))  ## Output: Chilcott
print(generated_function("Chong Aylward"))  ## Output: Aylward
print(generated_function("Jani Ramthun"))  ## Output: Ramthun
print(generated_function("Jacquiline Heintz"))  ## Output: Heintz
print(generated_function("Hayley Marquess"))  ## Output: Marquess
print(generated_function("Andria Spagnoli"))  ## Output: Spagnoli
print(generated_function("Irwin Covelli"))  ## Output: Covelli
print(generated_function("Gertude Montiel"))  ## Output: Montiel
print(generated_function("Stefany Reily"))  ## Output: Reily
print(generated_function("Rae Mcgaughey"))  ## Output: Mcgaughey
print(generated_function("Cruz Latimore"))  ## Output: Latimore
print(generated_function("Maryann Casler"))  ## Output: Casler
print(generated_function("Annalisa Gregori"))  ## Output: Gregori
print(generated_function("Jenee Pannell"))  ## Output: Pannell

# End time: 2024-04-09 13:28:30.897095
# Elapsed time in seconds: 10.132124123999347