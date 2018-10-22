import webbrowser as web
from Flashcards import *
from functions import *
from urllib.request import urlopen

# Initalize index counter
i = 0

# Print list of dict study options
print("Welche Kartenstapel möchtest du studieren?")
printList()
    
# Take user input on which dict to study
study_answer = input().lower()

# Ask to review or to study
print("Would you like to study or review?")
response = input().lower()

# Check for dict and then select if there
if study_answer in string_list_of_dictionaries:
    index = string_list_of_dictionaries.index(study_answer)

# Call the study function to begin listing dict elements
if response == 'review' or response == 'Review':
    review(list_of_dicts[index])
elif response == 'study' or response == 'Study':
    study(list_of_dicts[index])
