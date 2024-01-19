#!/usr/bin/env python3

import random
import time

def slow_print(text, delay=0.0):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    

def greeting():
    slow_print("You hear a mysterious, omnipotent voice echoing in his mind. Confused as you are, you can feel the overwhelming powerful yet calming presence.The voice introduces itself as the Guide of Elysium, an entity tasked with overseeing the reincarnation process of souls from different dimensions. The Guide explains that in Elysium, individuals have the opportunity to shape their destinies by rolling for their life stats.")
    slow_print(" *you hear a distinct cheerful voice* Hello! I know this is very sudden but im excited for you to begin your adventure! Ill be your guardian!")
    slow_print("You'll now spin the Wheel of Fate and be assigned stats for your adventure.")
    slow_print("Keep in mind the rolls are random with a minimum of 1 and maximum of 30. Each one of these stats will greatly impact your next life youre about to begin!")
    user_input = input("Whenever youre ready hit enter to continue!")
    combined_state = None
    combined_state = generate_stats()
    valid_input = False
    while not valid_input:
        if user_input == "":
           
            valid_input = True
            
        act1(combined_state)



def generate_stats():
    global wealth, health, intelligence, strength, charisma, agility, luck, adaptability
    
    wealth = random.randint(1, 30)
    health = random.randint(1, 30)
    intelligence = random.randint(1, 30)
    strength = random.randint(1, 30)
    charisma = random.randint(1,30)
    agility = random.randint(1, 30)
    luck = random.randint(1, 30)
    adaptability = random.randint(1, 30)
    
    wealth_state = ""
    if wealth <= 5:
        wealth_state = "You're born in a poor family."
    elif wealth <= 10:
        wealth_state = "You're from a lower middle class family."
    elif wealth <= 15:
        wealth_state = "You're from a middle class family."
    elif wealth <= 20:
        wealth_state = "You're from an upper middle class family."
    elif wealth <= 25:
        wealth_state = "You're from a wealthy family."
    else:
        wealth_state = "You're extremely rich."
    
    health_state = ""

    if health <= 5:
        health_state = "Very poor health." 
    elif health <= 10:
        health_state = "Poor health."
    elif health <= 15:
        health_state = "Fair health."
    elif health <= 20:
        health_state = "Good health."
    elif health <= 25:
        health_state = "Very good health."
    else:
        health_state = "Excellent health."
    
    intelligence_state = ""

    if intelligence <= 5:
        intelligence_state = "Very low intelligence."
    elif intelligence <= 10:
        intelligence_state = "Low intelligence."
    elif intelligence <= 15:
        intelligence_state = "Average intelligence."
    elif intelligence <= 20:
        intelligence_state = "Above average intelligence."
    elif intelligence <= 25:
        intelligence_state = "High intelligence."
    else:
        intelligence_state = "Exceptional intelligence."
        
    strength_state = ""
    if strength <= 5:
        strength_state = "Very weak."
    elif strength <= 10:
        strength_state = "Weak."
    elif strength <= 15:
        strength_state = "Average strength."
    elif strength <= 20:
        strength_state = "Strong."
    elif strength <= 25:
        strength_state = "Very strong."
    else:
        strength_state = "Exceptionally strong."
    
    charisma_state = ""
     
    if charisma <= 5:
        charisma_state = "Very low charisma."
    elif charisma <= 10:
        charisma_state = "Low charisma."
    elif charisma <= 15:
        charisma_state = "Average charisma."
    elif charisma <= 20:
        charisma_state = "High charisma."
    elif charisma <= 25:
        charisma_state = "Very high charisma."
    else:
        charisma_state = "Exceptional charisma."
    
    agility_state = ""

    if agility <= 5:
        agility_state = "Very low agility."
    elif agility <= 10:
        agility_state = "Low agility."
    elif agility <= 15:
        agility_state = "Average agility."
    elif agility <= 20:
        agility_state = "High agility."
    elif agility <= 25:
        agility_state = "Very high agility."
    else:
        agility_state = "Exceptional agility."

    luck_state = ""

    if luck <= 5:
        luck_state = "Very unlucky."
    elif luck <= 10:
        luck_state = "Unlucky."
    elif luck <= 15:
        luck_state = "Average luck."
    elif luck <= 20:
        luck_state = "Lucky."
    elif luck <= 25:
        luck_state = "Very lucky."
    else:
        luck_state = "Exceptionally lucky."

    adaptability_state = ""

    if adaptability <= 5:
        adaptability_state = "Very low adaptability."
    elif adaptability <= 10:
        adaptability_state = "Low adaptability."
    elif adaptability <= 15:
        adaptability_state = "Average adaptability."
    elif adaptability <= 20:
        adaptability_state = "High adaptability."
    elif adaptability <= 25:
        adaptability_state = "Very high adaptability."
    else:
        adaptability_state = "Exceptional adaptability."
    stat_sheet = {"Wealth": wealth, "Health": health, "Intelligence": intelligence, "Strength": strength, "Charisma": charisma, "Agility": agility, "Luck": luck, "Adaptability": adaptability}
    combined_state = {"Wealth": wealth_state, "Health": health_state, "Intelligence": intelligence_state, "Strength": strength_state, "Charisma": charisma_state, "Agility": agility_state, "Luck": luck_state, "Adaptability": adaptability_state}
    return combined_state


    

def act1(combined_state):
    
    slow_print("Guardian: Looks like your stats have been assigned. Lets take a look and see what you got!")
    for key, value in combined_state.items():
        print(f"{key}: {value}")
    slow_print("Guardian: At 18 years old youre faced with a decision. You can apply for college, enter the workforce at a local business, or set off to a big city for more opportunities!")
    slow_print("Guardian: It's time to make your first decision. Choose wisely.")
    user_choice = input("1. Apply for college\n2. Apply for a job\n3. Move to a big city.\n Your choice: ")

    if user_choice == "1":
        apply_college()
    elif user_choice == "2":
        apply_job()
    elif user_choice == "3":
       move_city()
    else:  slow_print("Guardian: Invalid choice. Please choose 1  2 or 3.")
          
    
def apply_college():
    slow_print("Guardian: Youve decided to enroll in an educational institution? Very well. Which type of institution would you like to apply for?")
    user_choice = input("1. Apply to community college\n2. Apply to public college\n 3. Apply to an elite private institution.\n Your choice: ")
    if user_choice == "1":
        community_college()
    elif user_choice == "2":
        public_college()
    elif user_choice == "3":
       ivy_league()
    else:  slow_print("Guardian: Invalid choice. Please choose 1  2 or 3.")
    
def apply_job():
    slow_print("Guardian: Youve decided to seek employment? Very well. You look into buisinesses hiring in your area. Which would you like to apply for?")
    user_choice= input("Seeing as you lack obvious workplace experience there are a few options that would work for you. 1. local supermarket. 2. restaurant dishwasher.")
    if user_choice == "1":
        local_supermarket()
    elif user_choice == "2":
        restaurant_staff()
    else: slow_print("Guardian: Invalid choice. Please choose 1 or 2.")

def move_city():
    slow_print("Guardian: Youve decided to move to a big city far from home. Adventurous and not shy a risk I see.")
    if luck >= 20 or wealth >=20:
        slow_print("You settle into your new surroundings fairly easily. You find an apartment and a part time job.")
    elif adaptability >= 15:
        slow_print("The journey was a little more difficult than you expected. You are struggling with your new enviroment but still excited for whats to come.")



def community_college():
    slow_print("You applied to a local community college. Now the time as has come. Youve received the letter by mail. You open the letter...")
    if intelligence >= 6 or adaptability >= 10:
        slow_print("You read the the letter. 'I am delighted to inform you  that the Committeee on Admissions has admitted you to the Class of ...'")
        
    
    
def public_college():
    slow_print("You applied to a well known public college. Now the time as has come. Youve received the letter by mail. You open the letter...")
    
    
    
def ivy_league():
    slow_print("You applied to the most prestigious institution available. Now the time as has come. Youve received the letter by mail. You open the letter...")
    if intelligence >= 25 or wealth >= 25:
        slow_print("You read the the letter. 'I am delighted to inform you  that the Committeee on Admissions has admitted you to the Class of ...'")
    elif intelligence >= 20 and luck >= 25:
         slow_print("You read the the letter. 'I am delighted to inform you  that the Committeee on Admissions has admitted you to the Class of ...'")
    else: slow_print("You read the letter. 'After careful consideration of your application. I am sorry to inform you...'")




def local_supermarket():
    print("")


def restaurant_staff():
    print("")



def main():
    greeting()
    act1()
    

main()
    
    
