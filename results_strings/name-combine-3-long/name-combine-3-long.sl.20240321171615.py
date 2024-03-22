def first_letter_period(input):
    first_name = input.split()[0]
    first_letter = first_name[0]
    last_name = input.split()[1]
    return f"{first_letter}. {last_name}"

# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

# Test cases
print(first_letter_period('Launa Withers'))  # L. Withers
print(first_letter_period('Lakenya Edison'))  # L. Edison
print(first_letter_period('Brendan Hage'))  # B. Hage
print(first_letter_period('Bradford Lango'))  # B. Lango
print(first_letter_period('Rudolf Akiyama'))  # R. Akiyama
print(first_letter_period('Lara Constable'))  # L. Constable
print(first_letter_period('Madelaine Ghoston'))  # M. Ghoston
print(first_letter_period('Salley Hornak'))  # S. Hornak
print(first_letter_period('Micha Junkin'))  # M. Junkin
print(first_letter_period('Teddy Bobo'))  # T. Bobo
print(first_letter_period('Coralee Scalia'))  # C. Scalia
print(first_letter_period('Jeff Quashie'))  # J. Quashie
print(first_letter_period('Vena Babiarz'))  # V. Babiarz
print(first_letter_period('Karrie Lain'))  # K. Lain
print(first_letter_period('Tobias Dermody'))  # T. Dermody
print(first_letter_period('Celsa Hopkins'))  # C. Hopkins
print(first_letter_period('Kimberley Halpern'))  # K. Halpern
print(first_letter_period('Phillip Rowden'))  # P. Rowden
print(first_letter_period('Elias Neil'))  # E. Neil
print(first_letter_period('Lashanda Cortes'))  # L. Cortes
print(first_letter_period('Mackenzie Spell'))  # M. Spell
print(first_letter_period('Kathlyn Eccleston'))  # K. Eccleston
print(first_letter_period('Georgina Brescia'))  # G. Brescia
print(first_letter_period('Beata Miah'))  # B. Miah
print(first_letter_period('Desiree Seamons'))  # D. Seamons
print(first_letter_period('Jeanice Soderstrom'))  # J. Soderstrom
print(first_letter_period('Mariel Jurgens'))  # M. Jurgens
print(first_letter_period('Alida Bogle'))  # A. Bogle
print(first_letter_period('Jacqualine Olague'))  # J. Olague
print(first_letter_period('Joaquin Clasen'))  # J. Clasen
print(first_letter_period('Samuel Richert'))  # S. Richert
print(first_letter_period('Malissa Marcus'))  # M. Marcus
print(first_letter_period('Alaina Partida'))  # A. Partida
print(first_letter_period('Trinidad Mulloy'))  # T. Mulloy
print(first_letter_period('Carlene Garrard'))  # C. Garrard
print(first_letter_period('Melodi Chism'))  # M. Chism
print(first_letter_period('Bess Chilcott'))  # B. Chilcott
print(first_letter_period('Chong Aylward'))  # C. Aylward
print(first_letter_period('Jani Ramthun'))  # J. Ramthun
print(first_letter_period('Jacquiline Heintz'))  # J. Heintz
print(first_letter_period('Hayley Marquess'))  # H. Marquess
print(first_letter_period('Andria Spagnoli'))  # A. Spagnoli
print(first_letter_period('Irwin Covelli'))  # I. Covelli
print(first_letter_period('Gertude Montiel'))  # G. Montiel
print(first_letter_period('Stefany Reily'))  # S. Reily
print(first_letter_period('Rae Mcgaughey'))  # R. Mcgaughey
print(first_letter_period('Cruz Latimore'))  # C. Latimore
print(first_letter_period('Maryann Casler'))  # M. Casler
print(first_letter_period('Annalisa Gregori'))  # A. Gregori
print(first_letter_period('Jenee Pannell'))  # J. Pannell
