def get_doctor_name(input_str):
    # Prompt: return "Dr. " and the first input after
    # Input: ['Launa Withers'] Output: Dr. Launa
    # Input: ['Lakenya Edison'] Output: Dr. Lakenya
    # Input: ['Brendan Hage'] Output: Dr. Brendan
    # Input: ['Bradford Lango'] Output: Dr. Bradford
    # Input: ['Rudolf Akiyama'] Output: Dr. Rudolf
    # Input: ['Lara Constable'] Output: Dr. Lara
    # Input: ['Madelaine Ghoston'] Output: Dr. Madelaine
    # Input: ['Salley Hornak'] Output: Dr. Salley
    # Input: ['Micha Junkin'] Output: Dr. Micha
    # Input: ['Teddy Bobo'] Output: Dr. Teddy
    # Input: ['Coralee Scalia'] Output: Dr. Coralee
    # Input: ['Jeff Quashie'] Output: Dr. Jeff
    # Input: ['Vena Babiarz'] Output: Dr. Vena
    # Input: ['Karrie Lain'] Output: Dr. Karrie
    # Input: ['Tobias Dermody'] Output: Dr. Tobias
    # Input: ['Celsa Hopkins'] Output: Dr. Celsa
    # Input: ['Kimberley Halpern'] Output: Dr. Kimberley
    # Input: ['Phillip Rowden'] Output: Dr. Phillip
    # Input: ['Elias Neil'] Output: Dr. Elias
    # Input: ['Lashanda Cortes'] Output: Dr. Lashanda
    # Input: ['Mackenzie Spell'] Output: Dr. Mackenzie
    # Input: ['Kathlyn Eccleston'] Output: Dr. Kathlyn
    # Input: ['Georgina Brescia'] Output: Dr. Georgina
    # Input: ['Beata Miah'] Output: Dr. Beata
    # Input: ['Desiree Seamons'] Output: Dr. Desiree
    # Input: ['Jeanice Soderstrom'] Output: Dr. Jeanice
    # Input: ['Mariel Jurgens'] Output: Dr. Mariel
    # Input: ['Alida Bogle'] Output: Dr. Alida
    # Input: ['Jacqualine Olague'] Output: Dr. Jacqualine
    # Input: ['Joaquin Clasen'] Output: Dr. Joaquin
    # Input: ['Samuel Richert'] Output: Dr. Samuel
    # Input: ['Malissa Marcus'] Output: Dr. Malissa
    # Input: ['Alaina Partida'] Output: Dr. Alaina
    # Input: ['Trinidad Mulloy'] Output: Dr. Trinidad
    # Input: ['Carlene Garrard'] Output: Dr. Carlene
    # Input: ['Melodi Chism'] Output: Dr. Melodi
    # Input: ['Bess Chilcott'] Output: Dr. Bess
    # Input: ['Chong Aylward'] Output: Dr. Chong
    # Input: ['Jani Ramthun'] Output: Dr. Jani
    # Input: ['Jacquiline Heintz'] Output: Dr. Jacquiline
    # Input: ['Hayley Marquess'] Output: Dr. Hayley
    # Input: ['Andria Spagnoli'] Output: Dr. Andria
    # Input: ['Irwin Covelli'] Output: Dr. Irwin
    # Input: ['Gertude Montiel'] Output: Dr. Gertude
    # Input: ['Stefany Reily'] Output: Dr. Stefany
    # Input: ['Rae Mcgaughey'] Output: Dr. Rae
    # Input: ['Cruz Latimore'] Output: Dr. Cruz
    # Input: ['Maryann Casler'] Output: Dr. Maryann
    # Input: ['Annalisa Gregori'] Output: Dr. Annalisa
    # Input: ['Jenee Pannell'] Output: Dr. Jenee
    
    return "Dr. " + input_str.split()[0]

# Test the function with an example input
input_str = 'Launa Withers'
output_str = get_doctor_name(input_str)
print(output_str)  # Output: Dr. Launa
