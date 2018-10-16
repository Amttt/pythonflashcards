from Flashcards import *
from functions import * 

print("Welche Kartenstapel möchtest du studieren?")
print('Halloween\nBirthdays\nStudies\nVerbs\nIrregular Verbs')
study_answer = input()

if study_answer.lower() == 'halloween':
    study(halloween)
elif study_answer.lower() == 'birthdays':
    study(birthdays)
elif study_answer.lower() == 'studies':
    study(studies)
elif study_answer.lower() == 'verbs':
    study(verbs)
elif study_answer.lower() == 'irregular verbs':
    study(irregular_verbs)

  

