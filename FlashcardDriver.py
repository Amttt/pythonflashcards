from Flashcards import *
from functions import * 

print("Welche Kartenstapel möchtest du studieren?")
print('Halloween\nBirthdays\nStudies\nVerbs\nIrregular Verbs\nAdjectives\n')
study_answer = input()

if study_answer in string_list_of_dictionaries:
    index = string_list_of_dictionaries.index(study_answer)
    study(list_of_dicts[index])
