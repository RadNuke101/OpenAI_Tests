# Function to return date and time from inputs
def get_date_time(input):
    # Split input by spaces
    input_list = input.split(" ")
    
    # Extract date and time from input list
    date = input_list[0] + " " + input_list[1] + " " + input_list[2]
    time = input_list[3]
    
    # Return date and time
    return date, time