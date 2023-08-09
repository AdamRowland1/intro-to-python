import random


def crossfitstart():
  # you should not have a capital letter at the start of your variable name when all other variableas start with a lower case letter!
  crossfit = ""
  while crossfit != "Yes" and crossfit != "No":
    crossfit = input("Do you partake in Crossfit? (Yes/No): ")
    if crossfit == "Yes":
      print("Amazing, let's find out how good you are!")
    elif crossfit == "No":
      print("That's disappointing, maybe you should give it ago.")
      return "No"
    else:
      print("Please respond with a Yes or No.")
  typeofcrossfitter = ""
  snatch = ""
  skills = ""
  computer_choice = random.choice([50, 75, 100])
  while typeofcrossfitter != "Lifter" and typeofcrossfitter != "Gymnast" and typeofcrossfitter != "Cardio Bunny":
    typeofcrossfitter = input(
      "What type of crossfitter are you? (Lifter/Gymnast/Cardio Bunny): ")
    if typeofcrossfitter == "Cardio Bunny":
      print('You are hard core')
    
    elif typeofcrossfitter == "Lifter":
      while snatch != "Yes" and snatch != "No":
        snatch = input("Do you snatch? (Yes/No): ")
        if snatch == "Yes":
          value = int(input("How much do you snatch?"))
          print(str(value) + " That's big!")
          print("Mine is " + str(computer_choice))
        elif snatch == "No":
          print("Ah Cleaning must be your thing.")
    
    elif typeofcrossfitter == "Gymnast":
      while skills != "Yes" and skills != "No":
        skills = input("Are you a gymnastic God? (Yes/No): ")
        if skills == "Yes":
          print('Would love to see you BMU, RMU or Handstand Walk')
        elif skills == "No":
          print("Best get practicing then")
          return "No"
        else:
          print("Please respond with a Yes or No.")
crossfitstart()
