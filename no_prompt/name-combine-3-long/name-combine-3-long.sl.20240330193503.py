# Start time: 2024-03-30 19:46:26.405321

# Content: Given that given input as ['Launa', 'Withers'] output is L. Withers, given input as ['Lakenya', 'Edison'] output is L. Edison, given input as ['Brendan', 'Hage'] output is B. Hage, given input as ['Bradford', 'Lango'] output is B. Lango, given input as ['Rudolf', 'Akiyama'] output is R. Akiyama, given input as ['Lara', 'Constable'] output is L. Constable, given input as ['Madelaine', 'Ghoston'] output is M. Ghoston, given input as ['Salley', 'Hornak'] output is S. Hornak, given input as ['Micha', 'Junkin'] output is M. Junkin, given input as ['Teddy', 'Bobo'] output is T. Bobo, given input as ['Coralee', 'Scalia'] output is C. Scalia, given input as ['Jeff', 'Quashie'] output is J. Quashie, given input as ['Vena', 'Babiarz'] output is V. Babiarz, given input as ['Karrie', 'Lain'] output is K. Lain, given input as ['Tobias', 'Dermody'] output is T. Dermody, given input as ['Celsa', 'Hopkins'] output is C. Hopkins, given input as ['Kimberley', 'Halpern'] output is K. Halpern, given input as ['Phillip', 'Rowden'] output is P. Rowden, given input as ['Elias', 'Neil'] output is E. Neil, given input as ['Lashanda', 'Cortes'] output is L. Cortes, given input as ['Mackenzie', 'Spell'] output is M. Spell, given input as ['Kathlyn', 'Eccleston'] output is K. Eccleston, given input as ['Georgina', 'Brescia'] output is G. Brescia, given input as ['Beata', 'Miah'] output is B. Miah, given input as ['Desiree', 'Seamons'] output is D. Seamons, given input as ['Jeanice', 'Soderstrom'] output is J. Soderstrom, given input as ['Mariel', 'Jurgens'] output is M. Jurgens, given input as ['Alida', 'Bogle'] output is A. Bogle, given input as ['Jacqualine', 'Olague'] output is J. Olague, given input as ['Joaquin', 'Clasen'] output is J. Clasen, given input as ['Samuel', 'Richert'] output is S. Richert, given input as ['Malissa', 'Marcus'] output is M. Marcus, given input as ['Alaina', 'Partida'] output is A. Partida, given input as ['Trinidad', 'Mulloy'] output is T. Mulloy, given input as ['Carlene', 'Garrard'] output is C. Garrard, given input as ['Melodi', 'Chism'] output is M. Chism, given input as ['Bess', 'Chilcott'] output is B. Chilcott, given input as ['Chong', 'Aylward'] output is C. Aylward, given input as ['Jani', 'Ramthun'] output is J. Ramthun, given input as ['Jacquiline', 'Heintz'] output is J. Heintz, given input as ['Hayley', 'Marquess'] output is H. Marquess, given input as ['Andria', 'Spagnoli'] output is A. Spagnoli, given input as ['Irwin', 'Covelli'] output is I. Covelli, given input as ['Gertude', 'Montiel'] output is G. Montiel, given input as ['Stefany', 'Reily'] output is S. Reily, given input as ['Rae', 'Mcgaughey'] output is R. Mcgaughey, given input as ['Cruz', 'Latimore'] output is C. Latimore, given input as ['Maryann', 'Casler'] output is M. Casler, given input as ['Annalisa', 'Gregori'] output is A. Gregori, given input as ['Jenee', 'Pannell'] output is J. Pannell, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        first_name, last_name = name.split()
        formatted_name = f"{first_name[0].upper()}. {last_name}"
        return formatted_name
    except (IndexError, ValueError):
        print("Invalid input format. Please provide a first name and a last name separated by a space.")

# Test cases
print(format_name('Launa Withers'))  # Output: L. Withers
print(format_name('Lakenya Edison'))  # Output: L. Edison
print(format_name('Brendan Hage'))  # Output: B. Hage
print(format_name('Bradford Lango'))  # Output: B. Lango
print(format_name('Rudolf Akiyama'))  # Output: R. Akiyama
print(format_name('Lara Constable'))  # Output: L. Constable
print(format_name('Madelaine Ghoston'))  # Output: M. Ghoston
print(format_name('Salley Hornak'))  # Output: S. Hornak
print(format_name('Micha Junkin'))  # Output: M. Junkin
print(format_name('Teddy Bobo'))  # Output: T. Bobo
print(format_name('Coralee Scalia'))  # Output: C. Scalia
print(format_name('Jeff Quashie'))  # Output: J. Quashie
print(format_name('Vena Babiarz'))  # Output: V. Babiarz
print(format_name('Karrie Lain'))  # Output: K. Lain
print(format_name('Tobias Dermody'))  # Output: T. Dermody
print(format_name('Celsa Hopkins'))  # Output: C. Hopkins
print(format_name('Kimberley Halpern'))  # Output: K. Halpern
print(format_name('Phillip Rowden'))  # Output: P. Rowden
print(format_name('Elias Neil'))  # Output: E. Neil
print(format_name('Lashanda Cortes'))  # Output: L. Cortes
print(format_name('Mackenzie Spell'))  # Output: M. Spell
print(format_name('Kathlyn Eccleston'))  # Output: K. Eccleston
print(format_name('Georgina Brescia'))  # Output: G. Brescia
print(format_name('Beata Miah'))  # Output: B. Miah
print(format_name('Desiree Seamons'))  # Output: D. Seamons
print(format_name('Jeanice Soderstrom'))  # Output: J. Soderstrom
print(format_name('Mariel Jurgens'))  # Output: M. Jurgens
print(format_name('Alida Bogle'))  # Output: A. Bogle
print(format_name('Jacqualine Olague'))  # Output: J. Olague
print(format_name('Joaquin Clasen'))  # Output: J. Clasen
print(format_name('Samuel Richert'))  # Output: S. Richert
print(format_name('Malissa Marcus'))  # Output: M. Marcus
print(format_name('Alaina Partida'))  # Output: A. Partida
print(format_name('Trinidad Mulloy'))  # Output: T. Mulloy
print(format_name('Carlene Garrard'))  # Output: C. Garrard
print(format_name('Melodi Chism'))  # Output: M. Chism
print(format_name('Bess Chilcott'))  # Output: B. Chilcott
print(format_name('Chong Aylward'))  # Output: C. Aylward
print(format_name('Jani Ramthun'))  # Output: J. Ramthun
print(format_name('Jacquiline Heintz'))  # Output: J. Heintz
print(format_name('Hayley Marquess'))  # Output: H. Marquess
print(format_name('Andria Spagnoli'))  # Output: A. Spagnoli
print(format_name('Irwin Covelli'))  # Output: I. Covelli
print(format_name('Gertude Montiel'))  # Output: G. Montiel
print(format_name('Stefany Reily'))  # Output: S. Reily
print(format_name('Rae Mcgaughey'))  # Output: R. Mcgaughey
print(format_name('Cruz Latimore'))  # Output: C. Latimore
print(format_name('Maryann Casler'))  # Output: M. Casler
print(format_name('Annalisa Gregori'))  # Output: A. Gregori
print(format_name('Jenee Pannell'))  # Output: J. Pannell

# End time: 2024-03-30 19:46:52.190199
# Elapsed time in seconds: 25.784603078000146