# Start time: 2024-03-30 23:01:26.440349

# Content: Given that given input as ['Launa', 'Withers'] output is Withers Launa, given input as ['Lakenya', 'Edison'] output is Edison Lakenya, given input as ['Brendan', 'Hage'] output is Hage Brendan, given input as ['Bradford', 'Lango'] output is Lango Bradford, given input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, given input as ['Lara', 'Constable'] output is Constable Lara, given input as ['Madelaine', 'Ghoston'] output is Ghoston Madelaine, given input as ['Salley', 'Hornak'] output is Hornak Salley, given input as ['Micha', 'Junkin'] output is Junkin Micha, given input as ['Teddy', 'Bobo'] output is Bobo Teddy, given input as ['Coralee', 'Scalia'] output is Scalia Coralee, given input as ['Jeff', 'Quashie'] output is Quashie Jeff, given input as ['Vena', 'Babiarz'] output is Babiarz Vena, given input as ['Karrie', 'Lain'] output is Lain Karrie, given input as ['Tobias', 'Dermody'] output is Dermody Tobias, given input as ['Celsa', 'Hopkins'] output is Hopkins Celsa, given input as ['Kimberley', 'Halpern'] output is Halpern Kimberley, given input as ['Phillip', 'Rowden'] output is Rowden Phillip, given input as ['Elias', 'Neil'] output is Neil Elias, given input as ['Lashanda', 'Cortes'] output is Cortes Lashanda, given input as ['Mackenzie', 'Spell'] output is Spell Mackenzie, given input as ['Kathlyn', 'Eccleston'] output is Eccleston Kathlyn, given input as ['Georgina', 'Brescia'] output is Brescia Georgina, given input as ['Beata', 'Miah'] output is Miah Beata, given input as ['Desiree', 'Seamons'] output is Seamons Desiree, given input as ['Jeanice', 'Soderstrom'] output is Soderstrom Jeanice, given input as ['Mariel', 'Jurgens'] output is Jurgens Mariel, given input as ['Alida', 'Bogle'] output is Bogle Alida, given input as ['Jacqualine', 'Olague'] output is Olague Jacqualine, given input as ['Joaquin', 'Clasen'] output is Clasen Joaquin, given input as ['Samuel', 'Richert'] output is Richert Samuel, given input as ['Malissa', 'Marcus'] output is Marcus Malissa, given input as ['Alaina', 'Partida'] output is Partida Alaina, given input as ['Trinidad', 'Mulloy'] output is Mulloy Trinidad, given input as ['Carlene', 'Garrard'] output is Garrard Carlene, given input as ['Melodi', 'Chism'] output is Chism Melodi, given input as ['Bess', 'Chilcott'] output is Chilcott Bess, given input as ['Chong', 'Aylward'] output is Aylward Chong, given input as ['Jani', 'Ramthun'] output is Ramthun Jani, given input as ['Jacquiline', 'Heintz'] output is Heintz Jacquiline, given input as ['Hayley', 'Marquess'] output is Marquess Hayley, given input as ['Andria', 'Spagnoli'] output is Spagnoli Andria, given input as ['Irwin', 'Covelli'] output is Covelli Irwin, given input as ['Gertude', 'Montiel'] output is Montiel Gertude, given input as ['Stefany', 'Reily'] output is Reily Stefany, given input as ['Rae', 'Mcgaughey'] output is Mcgaughey Rae, given input as ['Cruz', 'Latimore'] output is Latimore Cruz, given input as ['Maryann', 'Casler'] output is Casler Maryann, given input as ['Annalisa', 'Gregori'] output is Gregori Annalisa, given input as ['Jenee', 'Pannell'] output is Pannell Jenee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def rearrange_names(input_str):
    try:
        names = input_str.split()
        if len(names) != 2:
            raise ValueError("Input should contain exactly two names separated by a space")
        
        return names[1] + " " + names[0]
    
    except ValueError as ve:
        return str(ve)

# Test cases
"""
print(rearrange_names('Launa Withers'))  # Output: Withers Launa
print(rearrange_names('Lakenya Edison'))  # Output: Edison Lakenya
print(rearrange_names('Brendan Hage'))  # Output: Hage Brendan
print(rearrange_names('Bradford Lango'))  # Output: Lango Bradford
print(rearrange_names('Rudolf Akiyama'))  # Output: Akiyama Rudolf
print(rearrange_names('Lara Constable'))  # Output: Constable Lara
print(rearrange_names('Madelaine Ghoston'))  # Output: Ghoston Madelaine
print(rearrange_names('Salley Hornak'))  # Output: Hornak Salley
print(rearrange_names('Micha Junkin'))  # Output: Junkin Micha
print(rearrange_names('Teddy Bobo'))  # Output: Bobo Teddy
print(rearrange_names('Coralee Scalia'))  # Output: Scalia Coralee
print(rearrange_names('Jeff Quashie'))  # Output: Quashie Jeff
print(rearrange_names('Vena Babiarz'))  # Output: Babiarz Vena
print(rearrange_names('Karrie Lain'))  # Output: Lain Karrie
print(rearrange_names('Tobias Dermody'))  # Output: Dermody Tobias
print(rearrange_names('Celsa Hopkins'))  # Output: Hopkins Celsa
print(rearrange_names('Kimberley Halpern'))  # Output: Halpern Kimberley
print(rearrange_names('Phillip Rowden'))  # Output: Rowden Phillip
print(rearrange_names('Elias Neil'))  # Output: Neil Elias
print(rearrange_names('Lashanda Cortes'))  # Output: Cortes Lashanda
print(rearrange_names('Mackenzie Spell'))  # Output: Spell Mackenzie
print(rearrange_names('Kathlyn Eccleston'))  # Output: Eccleston Kathlyn
print(rearrange_names('Georgina Brescia'))  # Output: Brescia Georgina
print(rearrange_names('Beata Miah'))  # Output: Miah Beata
print(rearrange_names('Desiree Seamons'))  # Output: Seamons Desiree
print(rearrange_names('Jeanice Soderstrom'))  # Output: Soderstrom Jeanice
print(rearrange_names('Mariel Jurgens'))  # Output: Jurgens Mariel
print(rearrange_names('Alida Bogle'))  # Output: Bogle Alida
print(rearrange_names('Jacqualine Olague'))  # Output: Olague Jacqualine
print(rearrange_names('Joaquin Clasen'))  # Output: Clasen Joaquin
print(rearrange_names('Samuel Richert'))  # Output: Richert Samuel
print(rearrange_names('Malissa Marcus'))  # Output: Marcus Malissa
print(rearrange_names('Alaina Partida'))  # Output: Partida Alaina
print(rearrange_names('Trinidad Mulloy'))  # Output: Mulloy Trinidad
print(rearrange_names('Carlene Garrard'))  # Output: Garrard Carlene
print(rearrange_names('Melodi Chism'))  # Output: Chism Melodi
print(rearrange_names('Bess Chilcott'))  # Output: Chilcott Bess
print(rearrange_names('Chong Aylward'))  # Output: Aylward Chong
print(rearrange_names('Jani Ramthun'))  # Output: Ramthun Jani
print(rearrange_names('Jacquiline Heintz'))  # Output: Heintz Jacquiline
print(rearrange_names('Hayley Marquess'))  # Output: Marquess Hayley
print(rearrange_names('Andria Spagnoli'))  # Output: Spagnoli Andria
print(rearrange_names('Irwin Covelli'))  # Output: Covelli Irwin
print(rearrange_names('Gertude Montiel'))  # Output: Montiel Gertude
print(rearrange_names('Stefany Reily'))  # Output: Reily Stefany
print(rearrange_names('Rae Mcgaughey'))  # Output: Mcgaughey Rae
print(rearrange_names('Cruz Latimore'))  # Output: Latimore Cruz
print(rearrange_names('Maryann Casler'))  # Output: Casler Maryann
print(rearrange_names('Annalisa Gregori'))  # Output: Gregori Annalisa
print(rearrange_names('Jenee Pannell'))  # Output: Pannell Jenee
"""

# End time: 2024-03-30 23:01:37.323165
# Elapsed time in seconds: 10.882565597999928