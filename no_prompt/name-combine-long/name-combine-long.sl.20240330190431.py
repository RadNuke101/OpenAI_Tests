# Start time: 2024-03-30 19:13:44.340166

# Content: Given that given input as ['Launa', 'Withers'] output is Launa Withers, given input as ['Lakenya', 'Edison'] output is Lakenya Edison, given input as ['Brendan', 'Hage'] output is Brendan Hage, given input as ['Bradford', 'Lango'] output is Bradford Lango, given input as ['Rudolf', 'Akiyama'] output is Rudolf Akiyama, given input as ['Lara', 'Constable'] output is Lara Constable, given input as ['Madelaine', 'Ghoston'] output is Madelaine Ghoston, given input as ['Salley', 'Hornak'] output is Salley Hornak, given input as ['Micha', 'Junkin'] output is Micha Junkin, given input as ['Teddy', 'Bobo'] output is Teddy Bobo, given input as ['Coralee', 'Scalia'] output is Coralee Scalia, given input as ['Jeff', 'Quashie'] output is Jeff Quashie, given input as ['Vena', 'Babiarz'] output is Vena Babiarz, given input as ['Karrie', 'Lain'] output is Karrie Lain, given input as ['Tobias', 'Dermody'] output is Tobias Dermody, given input as ['Celsa', 'Hopkins'] output is Celsa Hopkins, given input as ['Kimberley', 'Halpern'] output is Kimberley Halpern, given input as ['Phillip', 'Rowden'] output is Phillip Rowden, given input as ['Elias', 'Neil'] output is Elias Neil, given input as ['Lashanda', 'Cortes'] output is Lashanda Cortes, given input as ['Mackenzie', 'Spell'] output is Mackenzie Spell, given input as ['Kathlyn', 'Eccleston'] output is Kathlyn Eccleston, given input as ['Georgina', 'Brescia'] output is Georgina Brescia, given input as ['Beata', 'Miah'] output is Beata Miah, given input as ['Desiree', 'Seamons'] output is Desiree Seamons, given input as ['Jeanice', 'Soderstrom'] output is Jeanice Soderstrom, given input as ['Mariel', 'Jurgens'] output is Mariel Jurgens, given input as ['Alida', 'Bogle'] output is Alida Bogle, given input as ['Jacqualine', 'Olague'] output is Jacqualine Olague, given input as ['Joaquin', 'Clasen'] output is Joaquin Clasen, given input as ['Samuel', 'Richert'] output is Samuel Richert, given input as ['Malissa', 'Marcus'] output is Malissa Marcus, given input as ['Alaina', 'Partida'] output is Alaina Partida, given input as ['Trinidad', 'Mulloy'] output is Trinidad Mulloy, given input as ['Carlene', 'Garrard'] output is Carlene Garrard, given input as ['Melodi', 'Chism'] output is Melodi Chism, given input as ['Bess', 'Chilcott'] output is Bess Chilcott, given input as ['Chong', 'Aylward'] output is Chong Aylward, given input as ['Jani', 'Ramthun'] output is Jani Ramthun, given input as ['Jacquiline', 'Heintz'] output is Jacquiline Heintz, given input as ['Hayley', 'Marquess'] output is Hayley Marquess, given input as ['Andria', 'Spagnoli'] output is Andria Spagnoli, given input as ['Irwin', 'Covelli'] output is Irwin Covelli, given input as ['Gertude', 'Montiel'] output is Gertude Montiel, given input as ['Stefany', 'Reily'] output is Stefany Reily, given input as ['Rae', 'Mcgaughey'] output is Rae Mcgaughey, given input as ['Cruz', 'Latimore'] output is Cruz Latimore, given input as ['Maryann', 'Casler'] output is Maryann Casler, given input as ['Annalisa', 'Gregori'] output is Annalisa Gregori, given input as ['Jenee', 'Pannell'] output is Jenee Pannell, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_names(names):
    try:
        first_name, last_name = names.split()
        return f"{first_name} {last_name}"
    except ValueError:
        return "Invalid input format. Please provide two names separated by a space."

# Test cases
print(format_names('Launa Withers'))  # Output: Launa Withers
print(format_names('Lakenya Edison'))  # Output: Lakenya Edison
print(format_names('Brendan Hage'))  # Output: Brendan Hage
print(format_names('Bradford Lango'))  # Output: Bradford Lango
print(format_names('Rudolf Akiyama'))  # Output: Rudolf Akiyama
print(format_names('Lara Constable'))  # Output: Lara Constable
print(format_names('Madelaine Ghoston'))  # Output: Madelaine Ghoston
print(format_names('Salley Hornak'))  # Output: Salley Hornak
print(format_names('Micha Junkin'))  # Output: Micha Junkin
print(format_names('Teddy Bobo'))  # Output: Teddy Bobo
print(format_names('Coralee Scalia'))  # Output: Coralee Scalia
print(format_names('Jeff Quashie'))  # Output: Jeff Quashie
print(format_names('Vena Babiarz'))  # Output: Vena Babiarz
print(format_names('Karrie Lain'))  # Output: Karrie Lain
print(format_names('Tobias Dermody'))  # Output: Tobias Dermody
print(format_names('Celsa Hopkins'))  # Output: Celsa Hopkins
print(format_names('Kimberley Halpern'))  # Output: Kimberley Halpern
print(format_names('Phillip Rowden'))  # Output: Phillip Rowden
print(format_names('Elias Neil'))  # Output: Elias Neil
print(format_names('Lashanda Cortes'))  # Output: Lashanda Cortes
print(format_names('Mackenzie Spell'))  # Output: Mackenzie Spell
print(format_names('Kathlyn Eccleston'))  # Output: Kathlyn Eccleston
print(format_names('Georgina Brescia'))  # Output: Georgina Brescia
print(format_names('Beata Miah'))  # Output: Beata Miah
print(format_names('Desiree Seamons'))  # Output: Desiree Seamons
print(format_names('Jeanice Soderstrom'))  # Output: Jeanice Soderstrom
print(format_names('Mariel Jurgens'))  # Output: Mariel Jurgens
print(format_names('Alida Bogle'))  # Output: Alida Bogle
print(format_names('Jacqualine Olague'))  # Output: Jacqualine Olague
print(format_names('Joaquin Clasen'))  # Output: Joaquin Clasen
print(format_names('Samuel Richert'))  # Output: Samuel Richert
print(format_names('Malissa Marcus'))  # Output: Malissa Marcus
print(format_names('Alaina Partida'))  # Output: Alaina Partida
print(format_names('Trinidad Mulloy'))  # Output: Trinidad Mulloy
print(format_names('Carlene Garrard'))  # Output: Carlene Garrard
print(format_names('Melodi Chism'))  # Output: Melodi Chism
print(format_names('Bess Chilcott'))  # Output: Bess Chilcott
print(format_names('Chong Aylward'))  # Output: Chong Aylward
print(format_names('Jani Ramthun'))  # Output: Jani Ramthun
print(format_names('Jacquiline Heintz'))  # Output: Jacquiline Heintz
print(format_names('Hayley Marquess'))  # Output: Hayley Marquess
print(format_names('Andria Spagnoli'))  # Output: Andria Spagnoli
print(format_names('Irwin Covelli'))  # Output: Irwin Covelli
print(format_names('Gertude Montiel'))  # Output: Gertude Montiel
print(format_names('Stefany Reily'))  # Output: Stefany Reily
print(format_names('Rae Mcgaughey'))  # Output: Rae Mcgaughey
print(format_names('Cruz Latimore'))  # Output: Cruz Latimore
print(format_names('Maryann Casler'))  # Output: Maryann Casler
print(format_names('Annalisa Gregori'))  # Output: Annalisa Gregori
print(format_names('Jenee Pannell'))  # Output: Jenee Pannell

# End time: 2024-03-30 19:13:53.090766
# Elapsed time in seconds: 8.750337316000241