import csv

#variables of individual data
pokemons = []
no = []
name = []
type1 = []
type2 = []
total = []
hp = []
attack = []
defense = []
sp_atk = []
sp_def = []
speed = []
generation = []
legendary = []


with open('Pokemon.csv', 'r') as file:
  reader = csv.reader(file)
  header = next(reader)
  header = list(header)
  for r in reader:
    #separating individual data into lists
    pokemons.append(r) #make nested list into separate rows of list
    no.append(r[0])
    name.append(r[1])
    type1.append(r[2])
    type2.append(r[3])
    total.append(r[4])
    hp.append(r[5])
    attack.append(r[6])
    defense.append(r[7])
    sp_atk.append(r[8])
    sp_def.append(r[9])
    speed.append(r[10])
    generation.append(r[11])
    legendary.append(r[12])

def printheader(): 
  print()
  print(f"{header[0]:<4}{header[1]:<26}{header[2]:<9}{header[3]:<9}{header[4]:<6}{header[5]:<6}{header[6]:<10}{header[7]:<10}{header[8]:<10}{header[9]:<10}{header[10]:<10}{header[11]:<12}{header[12]}")

def instructions():
  print("Pokemon Super Search Engine")
  print("1. Display Pokemon with their types and statistics")
  print("2. Display the first Pokemon of a type of your choice")
  print("3. Display all Pokemons with Total Base stat of your choice")
  print("4. Display all Pokemons with a minimum set of stats")
  print("5. Display all legendary Pokemons of specific Type1 and Type2")
  print("0. Quit")
  print()

def option1():
  '''This function displays n number of Pokemons with their types and statistics'''
  num = input("Enter number of Pokemons to be displayed: ")
  #error validation
  if num.isdigit() == False:
    print("Invalid input. Please enter a number.")

  elif int(num) == 0:
    print("Minimum number of Pokemon to be displayed is 1.")

  elif int(num) <= 800:
    data = []
    for item in pokemons[:int(num)]: #print until nth pokemon
      data.append(item)

    #output
    printheader()
    for lst in data:
      print(f"{lst[0]:<4}{lst[1]:<26}{lst[2]:<9}{lst[3]:<9}{lst[4]:<6}{lst[5]:<6}{lst[6]:<10}{lst[7]:<10}{lst[8]:<10}{lst[9]:<10}{lst[10]:<10}{lst[11]:<12}{lst[12]}")

  else:
    print("Exceeded maximum number of Pokemons. Maximum number of Pokemons is 800.")

def option2():
  '''This function displays the first Pokemon of a type inputted'''
  type = input("Enter type: ")
  type = type.capitalize()
  
  if type not in type1 and type2:
    print("No Pokemon of this type.")
  
  else:
    x1 = type1.index(type) #first occurence of the type in Type 1
    x2 = type2.index(type) #first occurence of the type in Type 2
    if x1 == -1: #if not found in Type 1
      x = x2
    elif x2 == -1: #if not found in Type 2
      x = x1
    else:
      x = x1 if x1 < x2 else x2 #if the type is found in Type 1 before Type 2, vice versa

    #output
    printheader()
    lst = pokemons[x]
    print(f"{lst[0]:<4}{lst[1]:<26}{lst[2]:<9}{lst[3]:<9}{lst[4]:<6}{lst[5]:<6}{lst[6]:<10}{lst[7]:<10}{lst[8]:<10}{lst[9]:<10}{lst[10]:<10}{lst[11]:<12}{lst[12]}")

def option3():
  '''This function displays all Pokemons with a total base stat inputted'''
  stat = input("Enter Total Base stat: ")

  if stat not in total:
    print("No Pokemon with this Total Base stat.")
  
  else:
    data = []
    for i in range(0, 800): #run the code from first pokemon to the last
      if total[i] == stat: #if stat of pokemon = stat inputted by user
        data.append(pokemons[i])

    #output
    printheader()
    for lst in data:
      print(f"{lst[0]:<4}{lst[1]:<26}{lst[2]:<9}{lst[3]:<9}{lst[4]:<6}{lst[5]:<6}{lst[6]:<10}{lst[7]:<10}{lst[8]:<10}{lst[9]:<10}{lst[10]:<10}{lst[11]:<12}{lst[12]}")
  
def option4():
  '''This function displays all Pokemons with a minimum set of stats inputted'''
  min_atk = input("Enter min special attack stat: ")
  min_def = input("Enter min special defense stat: ")
  min_speed = input("Enter min speed stat: ")
  condition = bool()
  data = []

  if min_atk.isdigit() == False or min_def.isdigit() == False or min_speed.isdigit() == False:
    print("Invalid input. Please enter a number.")

  else:
    for i in range(0, 800): #run the code from first pokemon to the last
      if int(sp_atk[i]) >= int(min_atk) and int(sp_def[i]) >= int(min_def) and int(speed[i]) >= int(min_speed):
        condition = True #if there's no pokemon with the minimum stats
        data.append(pokemons[i])
    
    #output
    if condition is not True: #if there's no pokemon with the minimum stats
      print("No Pokemon has such powerful stats.")
    
    else:
      printheader()
      for lst in data:
        print(f"{lst[0]:<4}{lst[1]:<26}{lst[2]:<9}{lst[3]:<9}{lst[4]:<6}{lst[5]:<6}{lst[6]:<10}{lst[7]:<10}{lst[8]:<10}{lst[9]:<10}{lst[10]:<10}{lst[11]:<12}{lst[12]}")
      
def option5():
  type_1 = input("Enter Type 1: ")
  type_2 = input("Enter Type 2: ")
  type_1 = type_1.capitalize()
  type_2 = type_2.capitalize()
  condition = bool()
  data = []
  
  for i in range(0, 800):
    if type_1 in type1[i] and type_2 in type2[i] and legendary[i] == "TRUE":
        condition = True
        data.append(pokemons[i])

  #output
  if condition is not True:
    print("No legendary Pokemon of this type.")
  else:
    for lst in data:
      print(f"{lst[0]:<4}{lst[1]:<26}{lst[2]:<9}{lst[3]:<9}{lst[4]:<6}{lst[5]:<6}{lst[6]:<10}{lst[7]:<10}{lst[8]:<10}{lst[9]:<10}{lst[10]:<10}{lst[11]:<12}{lst[12]}")

def surprise():
  username = input("Wait! Before you go, what's your first name? ")
  initial = username[0]
  initial = initial.capitalize()
  data = []
  for i in range(800):
    if initial == name[i][0]:
      data.append(pokemons[i])

  print("These Pokemons have the same initial as you!")
  printheader()
  for lst in data:
    print(f"{lst[0]:<4}{lst[1]:<26}{lst[2]:<9}{lst[3]:<9}{lst[4]:<6}{lst[5]:<6}{lst[6]:<10}{lst[7]:<10}{lst[8]:<10}{lst[9]:<10}{lst[10]:<10}{lst[11]:<12}{lst[12]}")

#start of program display ------------------------------

instructions() #print instructions
option = input("Enter option: ")

while option != "0": #loop program until user quits
  if option == "1":
    option1()
  if option == "2":
    option2()
  if option == "3":
    option3()
  if option == "4":
    option4()
  if option == "5":
    option5()
  if option != "1" and option != "2" and option != "3" and option != "4" and option != "5":
    print("Please choose a valid option.")

  print()
  instructions()
  option = input("Enter option: ")

if option == "0":
  surprise()
  print("\nBye! Thank you for using Pokemon Super Search Engine.")