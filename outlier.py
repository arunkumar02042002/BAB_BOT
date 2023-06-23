# Importing the random module
import random

def random_ans():
    # Function to generate a random answer from a list of predefined responses
    random_list = [
        "I can't answer that yet, please try asking something else.",
        "I think you have entered something I don't understand.",
        "Can you please tell me more on this?",
        "I'm not able to figure it out what you are trying to say."
    ]

    # Get the number of items in the random_list
    list_count = len(random_list)

    # Generate a random index within the range of items
    random_item = random.randrange(list_count)
    
    # Return a randomly selected response
    return random_list[random_item]