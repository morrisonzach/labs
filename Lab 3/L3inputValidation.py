#
#   purpose: to mix two colors together and
#            maintain input validation
#   author: zachary morrison
#   date written: 09/20/2020
#   Version: 1.0.0
#

#   background
print('When you mix red and blue, you get purple.')
print('When you mix red and yellow, you get orange.')
print('When you mix blue and yellow, you get green.')
print('\n--------------------------------------------\n')
print('Options: [red, yellow, blue]\n')

#   input
color1 = input('Enter the first color you\'d like to mix:\t')
color2 = input('Enter the second color you\'d like to mix:\t')

#   processing and output
if ((color1.lower() == "red") or (color1.lower() == "blue") or (color1.lower() == "yellow")) and ((color2.lower() == "red") or (color2.lower() == "blue") or (color2.lower() == "yellow")):
    if color1.lower() == "red":
        if color2.lower() == "blue":
            print("\nWhen you mix red and blue, you get purple.")
        elif color2.lower() == "yellow":
            print("\nWhen you mix red and yellow, you get orange.")
        else:
            print("\nYou input red twice!")
    elif color1.lower() == "blue":
        if color2.lower() == "red":
            print("\nWhen you mix red and blue, you get purple.")
        elif color2.lower() == "yellow":
            print("\nWhen you mix blue and yellow, you get green.")
        else:
            print("\nYou input blue twice!")
    else:
        if color2.lower() == "red":
            print("\nWhen you mix red and yellow, you get orange.")
        elif color2.lower() == "blue":
            print("\nWhen you mix blue and yellow, you get green.")
        else:
            print("\nYou input yellow twice!")
else:
    print("\nYou didn't input two primary colors.")
