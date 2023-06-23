# Importing necessary packages
import re
import json
import outlier
import time

# Defining the get_data function:
def get_data(file_name):
    # Function to read data from a JSON file
    # and return it as a Python object
    with open(file_name, "r") as f:
        return json.load(f)

# Load data from the "response.json" file
data = get_data("responses.json")

# Defining the get_result function:
def get_result(users_message):

    # Splitting the user's message into a list of words
    word_list = re.split(r"\s+|[,;?'!.-]\s*", users_message)
    score_list = []  # List to store the scores for each response

    for response in data:
        required_score = 0
        response_score = 0
        # Get the required keywords for the response
        requiredKeywords = response["requiredKeywords"]

        if requiredKeywords:
            # Check if the user's message contains all the required keywords
            for word in requiredKeywords:
                if word in users_message:
                    required_score += 1

        if required_score == len(requiredKeywords):
            # If all the required keywords are present,
            # calculate the response score based on user input matches
            for word in response["usersInput"]:
                if word in word_list:
                    response_score += 1

        # Add the response score to the list of scores
        score_list.append(response_score)
    # Find the highest score
    highest_score = max(score_list)

    if highest_score != 0:
        best_index = score_list.index(highest_score)
        # Return the best response based on the highest score
        return data[best_index]["BAB_BOT_Answer"]

    # If no response matches the criteria,
    # generate a random response using the outlier module
    return outlier.random_ans()

# Defining the type_message function:
def type_message(message, delay=0.01):

    # Function to simulate typing a message
    # by printing each character with a small delay
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a newline character at the end

# Main program execution:
if __name__ == "__main__":
    with open("initial.txt", 'r') as f:
        # Display the content of the "initial.txt" file
        type_message(f.read())

    while True:
        # Get user input and convert it to lowercase
        users_input = input("You: ").lower()

        if users_input == "":
            type_message(
                "BOT: I like talking to you even when we have nothing to say! You can ask me anything!")
            continue  # Continue the conversation if the user input is empty

        if users_input == '0':
            type_message("BOT: I like talking to you even when we have nothing to say!")
            break  # End the conversation if the user enters '0'

        # Get the appropriate response based on the user input
        response = get_result(users_input)

        # Print the response with "Bot:" as a prefix
        print("Bot:", end=" ")
        type_message(response)