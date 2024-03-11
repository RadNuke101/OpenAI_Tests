#Python program to return the first decimal (from the left) to the tenths place

#Function to return first decimal
def return_first_decimal(input):
    #Split input by space
    split_input = input.split(" ")
    #Initialize decimal variable
    decimal = ""
    #Loop through elements in split_input
    for element in split_input:
        #Check if element is a number
        if element.isdigit():
            #Add decimal point
            decimal += "." + element
    #Return the decimal rounded to the tenths place
    return round(float(decimal[1:]), 1)