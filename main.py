# # 

# height= float(input('what is your height? '))
# bill=0
# if height>=120:
    

#     age =int(input('what is your age: '))

#     if age<=10:
            
# 			 bill= 2
#         print('age of people below 10')
		
#     elif age>=10 and age<20:
# 	    bill= 3
# 	    print('age of people above 10')
	
#     else:
# 	    bill= 4
# 	    print('age of people above 20')

#     Total_bill= input('Do you want the Total Bill: y or n')

#     if Total_bill=="y":
# 	    bill+=10
# 	    print(f'your total bill is ${bill}')
# else:
#     print('too short')


# heigth = float(input('What is your height? '))
# bill= 0

# if heigth >=120:

# 	age= int(input("what is your age? "))
	
# 	if age<=10:
# 			bill=10
# 			print("Age is below 10")

# 	elif age>10 and age<=20:
# 			bill=20
# 			print('Age is between 10 and 20')

# 	else:
# 			bill=30
# 			print('age is older')

# 	Ticket = input('do you want a ticket? y or n')
# 	if Ticket=='y':
# 			bill+=3
# 			print(f'your final bill ${bill}')

# else:
# 	print('Your are below the height range.')

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
	
print ('Welcome to Treasure Island.')
print ('Your mission is to find the treasure.')

choice_of_path= input('Your path begins on a road, you have a choice, go "Left" and discover what destine has install or go "Right" to find the treasure? ')

if choice_of_path== 'Right' or choice_of_path== 'right':
		print('You fell into lava while carrying the gold. Game Over.')

elif choice_of_path=='Left' or choice_of_path== 'left':
	choice_of_movement= input('You have arrived at the lake of mystery. Do you  Choose to "swim", the healing of the water will purify  or "Wait" and discover the path unfold? ')
	if choice_of_movement== 'Swim' or choice_of_movement== 'swim':
			print('The waters are steep and your soul cleansed from its shell. Game Over.')

			
	elif choice_of_movement=='Wait' or choice_of_movement== 'wait':
		choice_of_door= input('Three doors lay on your path to that Which you seek, make your pick and uncover fate door? Blue or Red or Yellow? ')

		if choice_of_door=='Blue' or  choice_of_door=='blue':
						print('Game over.')

		elif choice_of_door=='Red' or  choice_of_door=='red':
						print('Game Over.')

		elif choice_of_door=='Yellow' or choice_of_door=='yellow':
						print('You Win!')
			
