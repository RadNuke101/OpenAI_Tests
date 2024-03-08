#Python program to return the first decimal (from the left) to the tenths place

#Initialize inputs
input_1 = "AIX 5.1"
input_2 = "VMware ESX Server 3.5.0 build-110268"
input_3 = "Linux Linux 2.6 Linux"
input_4 = "Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>"
input_5 = "Microsoft <R> Windows <R> 2000 Advanced Server 1.0"
input_6 = "Microsoft Windows XP Win2008R2 6.1.7601"

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

#Print outputs
print(return_first_decimal(input_1))
print(return_first_decimal(input_2))
print(return_first_decimal(input_3))
print(return_first_decimal(input_4))
print(return_first_decimal(input_5))
print(return_first_decimal(input_6))