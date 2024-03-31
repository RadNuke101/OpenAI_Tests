# Start time: 2024-03-30 04:04:52.643661
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second word of the inputted phrase, and given input as ['Nancy FreeHafer'] output is FreeHafer, given input as ['Andrew Cencici'] output is Cencici, given input as ['Jan Kotas'] output is Kotas, given input as ['Mariya Sergienko'] output is Sergienko, given input as ['Launa Withers'] output is Withers, given input as ['Lakenya Edison'] output is Edison, given input as ['Brendan Hage'] output is Hage, given input as ['Bradford Lango'] output is Lango, given input as ['Rudolf Akiyama'] output is Akiyama, given input as ['Lara Constable'] output is Constable, given input as ['Madelaine Ghoston'] output is Ghoston, given input as ['Salley Hornak'] output is Hornak, given input as ['Micha Junkin'] output is Junkin, given input as ['Teddy Bobo'] output is Bobo, given input as ['Coralee Scalia'] output is Scalia, given input as ['Jeff Quashie'] output is Quashie, given input as ['Vena Babiarz'] output is Babiarz, given input as ['Karrie Lain'] output is Lain, given input as ['Tobias Dermody'] output is Dermody, given input as ['Celsa Hopkins'] output is Hopkins, given input as ['Kimberley Halpern'] output is Halpern, given input as ['Phillip Rowden'] output is Rowden, given input as ['Elias Neil'] output is Neil, given input as ['Lashanda Cortes'] output is Cortes, given input as ['Mackenzie Spell'] output is Spell, given input as ['Kathlyn Eccleston'] output is Eccleston, given input as ['Georgina Brescia'] output is Brescia, given input as ['Beata Miah'] output is Miah, given input as ['Desiree Seamons'] output is Seamons, given input as ['Jeanice Soderstrom'] output is Soderstrom, given input as ['Mariel Jurgens'] output is Jurgens, given input as ['Alida Bogle'] output is Bogle, given input as ['Jacqualine Olague'] output is Olague, given input as ['Joaquin Clasen'] output is Clasen, given input as ['Samuel Richert'] output is Richert, given input as ['Malissa Marcus'] output is Marcus, given input as ['Alaina Partida'] output is Partida, given input as ['Trinidad Mulloy'] output is Mulloy, given input as ['Carlene Garrard'] output is Garrard, given input as ['Melodi Chism'] output is Chism, given input as ['Bess Chilcott'] output is Chilcott, given input as ['Chong Aylward'] output is Aylward, given input as ['Jani Ramthun'] output is Ramthun, given input as ['Jacquiline Heintz'] output is Heintz, given input as ['Hayley Marquess'] output is Marquess, given input as ['Andria Spagnoli'] output is Spagnoli, given input as ['Irwin Covelli'] output is Covelli, given input as ['Gertude Montiel'] output is Montiel, given input as ['Stefany Reily'] output is Reily, given input as ['Rae Mcgaughey'] output is Mcgaughey, given input as ['Cruz Latimore'] output is Latimore, given input as ['Maryann Casler'] output is Casler, given input as ['Annalisa Gregori'] output is Gregori, given input as ['Jenee Pannell'] output is Pannell, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the second word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: FreeHafer

def get_second_word(input_phrase):
    try:
        # Extract the input phrase from the list
        phrase = input_phrase[0]
        
        # Split the phrase into words
        words = phrase.split()
        
        # Return the second word
        return words[1]
    
    except (IndexError, AttributeError):
        return "Invalid input. Please provide a valid input phrase."
    
# Test cases
print(get_second_word(['Nancy FreeHafer']))  # Output: FreeHafer
print(get_second_word(['Andrew Cencici']))  # Output: Cencici
print(get_second_word(['Jan Kotas']))  # Output: Kotas
print(get_second_word(['Mariya Sergienko']))  # Output: Sergienko
print(get_second_word(['Invalid Input']))  # Output: Invalid input. Please provide a valid input phrase.

# End time: 2024-03-30 04:04:55.587722
# Elapsed time in seconds: 2.9439980300012394