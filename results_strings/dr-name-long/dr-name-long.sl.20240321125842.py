# Prompt: return "Dr. " and the first input after
# Given input as ['Launa Withers'] output is Dr. Launa
# Given input as ['Lakenya Edison'] output is Dr. Lakenya
# Given input as ['Brendan Hage'] output is Dr. Brendan
# Given input as ['Bradford Lango'] output is Dr. Bradford
# Given input as ['Rudolf Akiyama'] output is Dr. Rudolf
# Given input as ['Lara Constable'] output is Dr. Lara
# Given input as ['Madelaine Ghoston'] output is Dr. Madelaine
# Given input as ['Salley Hornak'] output is Dr. Salley
# Given input as ['Micha Junkin'] output is Dr. Micha
# Given input as ['Teddy Bobo'] output is Dr. Teddy
# Given input as ['Coralee Scalia'] output is Dr. Coralee
# Given input as ['Jeff Quashie'] output is Dr. Jeff
# Given input as ['Vena Babiarz'] output is Dr. Vena
# Given input as ['Karrie Lain'] output is Dr. Karrie
# Given input as ['Tobias Dermody'] output is Dr. Tobias
# Given input as ['Celsa Hopkins'] output is Dr. Celsa
# Given input as ['Kimberley Halpern'] output is Dr. Kimberley
# Given input as ['Phillip Rowden'] output is Dr. Phillip
# Given input as ['Elias Neil'] output is Dr. Elias
# Given input as ['Lashanda Cortes'] output is Dr. Lashanda
# Given input as ['Mackenzie Spell'] output is Dr. Mackenzie
# Given input as ['Kathlyn Eccleston'] output is Dr. Kathlyn
# Given input as ['Georgina Brescia'] output is Dr. Georgina
# Given input as ['Beata Miah'] output is Dr. Beata
# Given input as ['Desiree Seamons'] output is Dr. Desiree
# Given input as ['Jeanice Soderstrom'] output is Dr. Jeanice
# Given input as ['Mariel Jurgens'] output is Dr. Mariel
# Given input as ['Alida Bogle'] output is Dr. Alida
# Given input as ['Jacqualine Olague'] output is Dr. Jacqualine
# Given input as ['Joaquin Clasen'] output is Dr. Joaquin
# Given input as ['Samuel Richert'] output is Dr. Samuel
# Given input as ['Malissa Marcus'] output is Dr. Malissa
# Given input as ['Alaina Partida'] output is Dr. Alaina
# Given input as ['Trinidad Mulloy'] output is Dr. Trinidad
# Given input as ['Carlene Garrard'] output is Dr. Carlene
# Given input as ['Melodi Chism'] output is Dr. Melodi
# Given input as ['Bess Chilcott'] output is Dr. Bess
# Given input as ['Chong Aylward'] output is Dr. Chong
# Given input as ['Jani Ramthun'] output is Dr. Jani
# Given input as ['Jacquiline Heintz'] output is Dr. Jacquiline
# Given input as ['Hayley Marquess'] output is Dr. Hayley
# Given input as ['Andria Spagnoli'] output is Dr. Andria
# Given input as ['Irwin Covelli'] output is Dr. Irwin
# Given input as ['Gertude Montiel'] output is Dr. Gertude
# Given input as ['Stefany Reily'] output is Dr. Stefany
# Given input as ['Rae Mcgaughey'] output is Dr. Rae
# Given input as ['Cruz Latimore'] output is Dr. Cruz
# Given input as ['Maryann Casler'] output is Dr. Maryann
# Given input as ['Annalisa Gregori'] output is Dr. Annalisa
# Given input as ['Jenee Pannell'] output is Dr. Jenee

def add_title(input_str):
    name = input_str.split()[0]
    return "Dr. " + name

# Test cases
print(add_title('Launa Withers'))  # Output: Dr. Launa
print(add_title('Lakenya Edison'))  # Output: Dr. Lakenya
print(add_title('Brendan Hage'))  # Output: Dr. Brendan
print(add_title('Bradford Lango'))  # Output: Dr. Bradford
print(add_title('Rudolf Akiyama'))  # Output: Dr. Rudolf
