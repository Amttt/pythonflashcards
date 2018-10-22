import webbrowser as web
import requests
from urllib.request import urlopen
from Flashcards import *

# Main function for studying a dict

def study(dictionary): # Takes input of a dict
    i = 0
    l = len(dictionary)
    while i < l:
        correct = False
        for key in dictionary:
            while correct == False:
                print(key)
                answer = input()
                if answer == dictionary[key]:
                    print('Korrekt!')
                    break
                elif answer == "hilfe" or answer == "Hilfe":
                    getHelp(key)
                else:
                    print('Inkorrekt!')
                    correct = False

# Main function for reviewing a dict   
def review(dictionary): # Takes input of a dict
    i = 0
    l = len(dictionary)
    while i < l:
        for key in dictionary:
                print("Deutsch: " + key + "\nEnglisch: " + dictionary[key])
                answer = input()
                if answer == 'done':
                    break

# Function to print list of available dicts for study                
def printList(): # No input necessary
    i = 0
    for name in string_list_of_dictionaries:
        print(string_list_of_dictionaries[i].title())
        i += 1

def encode(word):
    word = word.replace(' ', '%20')
    word = word.replace('ä', '%C3%A4')
    word = word.replace('Ä', '%C3%84')
    word = word.replace('ë', '%C3%AB')
    word = word.replace('Ë', '%C3%8B')
    word = word.replace('ö', '%C3%B6')
    word = word.replace('Ö', '%C3%96')
    word = word.replace('ü','%C3%BC')
    word = word.replace('Ü','%C3%9C')
    word = word.replace('ß','%C3%9F')
    return word

# Function to open webpage to German dictionary for help
def getHelp(word):
    word = encode(word)
    url = 'https://dict.leo.org/german-english/' + word ### Curent issue with ascii and utf-8
    web.open(url)


    





    

                
    
