# to convert height in feet and inches to cm

inch = int(input('Enter height in inches : '))
feet = int(input('Enter height in feet : '))

total_inches = (feet * 12) + inch
cm = total_inches * 2.54

print('Height in cm =', cm)
