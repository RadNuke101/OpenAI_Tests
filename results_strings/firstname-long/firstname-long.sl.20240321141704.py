def get_first_word(input_str):
    return input_str.split()[0]

# Prompt: return the first word of the inputted phrase
# input: ['Nancy FreeHafer'] output: Nancy
# input: ['Andrew Cencici'] output: Andrew
# input: ['Jan Kotas'] output: Jan
# input: ['Mariya Sergienko'] output: Mariya
# input: ['Launa Withers'] output: Launa
# input: ['Lakenya Edison'] output: Lakenya
# input: ['Brendan Hage'] output: Brendan
# input: ['Bradford Lango'] output: Bradford
# input: ['Rudolf Akiyama'] output: Rudolf
# input: ['Lara Constable'] output: Lara
# input: ['Madelaine Ghoston'] output: Madelaine
# input: ['Salley Hornak'] output: Salley
# input: ['Micha Junkin'] output: Micha
# input: ['Teddy Bobo'] output: Teddy
# input: ['Coralee Scalia'] output: Coralee
# input: ['Jeff Quashie'] output: Jeff
# input: ['Vena Babiarz'] output: Vena
# input: ['Karrie Lain'] output: Karrie
# input: ['Tobias Dermody'] output: Tobias
# input: ['Celsa Hopkins'] output: Celsa
# input: ['Kimberley Halpern'] output: Kimberley
# input: ['Phillip Rowden'] output: Phillip
# input: ['Elias Neil'] output: Elias
# input: ['Lashanda Cortes'] output: Lashanda
# input: ['Mackenzie Spell'] output: Mackenzie
# input: ['Kathlyn Eccleston'] output: Kathlyn
# input: ['Georgina Brescia'] output: Georgina
# input: ['Beata Miah'] output: Beata
# input: ['Desiree Seamons'] output: Desiree
# input: ['Jeanice Soderstrom'] output: Jeanice
# input: ['Mariel Jurgens'] output: Mariel
# input: ['Alida Bogle'] output: Alida
# input: ['Jacqualine Olague'] output: Jacqualine
# input: ['Joaquin Clasen'] output: Joaquin
# input: ['Samuel Richert'] output: Samuel
# input: ['Malissa Marcus'] output: Malissa
# input: ['Alaina Partida'] output: Alaina
# input: ['Trinidad Mulloy'] output: Trinidad
# input: ['Carlene Garrard'] output: Carlene
# input: ['Melodi Chism'] output: Melodi
# input: ['Bess Chilcott'] output: Bess
# input: ['Chong Aylward'] output: Chong
# input: ['Jani Ramthun'] output: Jani
# input: ['Jacquiline Heintz'] output: Jacquiline
# input: ['Hayley Marquess'] output: Hayley
# input: ['Andria Spagnoli'] output: Andria
# input: ['Irwin Covelli'] output: Irwin
# input: ['Gertude Montiel'] output: Gertude
# input: ['Stefany Reily'] output: Stefany
# input: ['Rae Mcgaughey'] output: Rae
# input: ['Cruz Latimore'] output: Cruz
# input: ['Maryann Casler'] output: Maryann
# input: ['Annalisa Gregori'] output: Annalisa
# input: ['Jenee Pannell'] output: Jenee

# Test the function
print(get_first_word('Nancy FreeHafer'))  # Output: Nancy
print(get_first_word('Andrew Cencici'))  # Output: Andrew
print(get_first_word('Jan Kotas'))  # Output: Jan
