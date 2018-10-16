# Main function for stuying a dictionary

def study(dictionary): # Takes input of a dictionary
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
                else:
                    print('Inkorrekt!')
                    correct = False
