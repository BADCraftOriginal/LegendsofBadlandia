import time
import os

global role

version = "0.25"
release = "BETA"
num = "1"

def intro():
    ## This part of the code is for
    ## the player to pick one of three
    ## classes:
    ##
    ## Warrior, Thief, Medic

    print("+------------------+")
    print("LEGENDS OF BADLANDIA")
    print("+------------------+")
    print("")
    time.sleep(1.5)
    print("VERSION",version,"-",release,num)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Monk Owen - Welcome, brother. As your new,")
    print("            I only find it right that i help")
    print("            establish you here.")
    time.sleep(4.43)
    print("Monk Owen - What is your name, young one?")
    time.sleep(0.99)
    name = input("You - My name is ")
    time.sleep(1.75)
    print("Monk Owen - Hold on.. What is your gender, Male or Female?")
    time.sleep(0.9)
    gensel = input("You - I am a ")
    time.sleep(2)
    print("Monk Owen - and a fine",gensel,"you are, too!")
    time.sleep(1.75)
    print("            I have 2 roles That suit your criteria.")
    print("            Chose wisely, you cant change this later!")
    time.sleep(2)
    print("1 - Thief")
    time.sleep(0.5)
    print("3 - Warrior")
    time.sleep(1)
    
    rolesel = input("You - I'd like option ")
    if rolesel == "1":
        #Thief
        time.sleep(0.5)
        print("Monk Owen - Thats a dark route.. I can't help you from now on..")
        time.sleep(2)
        Thiefintro()
    
    elif rolesel == "2":
        #Warrior
        time.sleep(0.5)
        print("Monk Owen - The most courageous of routes to choose.. Good on you,",name,"!")
        time.sleep(2)
        Warriorintro()

    else:
        print("Monk Owen - Sorry, there isnt a number",rolesel,"!")
        roleselection()
        
#Thief
        
def Thiefintro():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("You walk over to the bar to order a drink.")
    time.sleep(1)
    print("As you look around you see a man staring at you.")
    time.sleep(1)
    print("What will you do?")
    print("1.Ask him what he's looking at.")
    print("2.Stare back.")
    print("3.Ignore him and order a drink.")
    choice = input(">>>")
    if choice == "1":
        Thiefone()
    elif choice == "2":
        Thieftwo()
    elif choice == "3":
        Thiefthree()

def Thiefone():
    print("You - What do you think your looking at?")
    time.sleep(1)
    print("Man - Want this to get nasty?")
    time.sleep (1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Punch him.")
    print("2.Ignore him.")
    print("3.Walk away.")
    choice = input(">>>")
    if choice == "1":
        Thiefone_one()
    elif choice == "2":
        Thiefthree()
    elif choice == "3":
        Thiefone_three()

def Thieftwo():
    print("Man - I haven't seen you here before.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Yeah, I just arrived today.")
    print("2.Do you want to join me for a drink?")
    print("3.What's it to you?")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one()
    elif choice == "2":
        Thieftwo_two()
    elif choice == "3":
        two_three()

def Thiefthree():
    print("As you order a drink you feel a tap")
    print("on your back. You turn around and see it's the man.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Ask him what he wants.")
    print("2.Ignore him.")
    choice = input(">>>")
    if choice == "1":
        Thiefthree_one()
    elif choice == "2":
        Thiefthree_two()

def Thiefone_one():
    print("You punch the man. He gets up straight away.")
    time.sleep(1)
    print("And he says:")
    time.sleep(0.5)
    print("Man - Good punch. We need someone like you.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1. Someone like me?")
    print("2. What for?")
    choice = input(">>>")
    if choice == "1":
        Thiefone_one_one()
    elif choice == "2":
        Thieftwo_one_one()

def Thiefone_three():
    print("As you walk away you feel a tap")
    print("on your back. You turn around and see it's the man.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Ask him what he wants.")
    choice = input(">>>")
    if choice == "1":
        Thiefone_three()

def Thieftwo_one():
    print("You - Yeah I just arrived today.")
    time.sleep(1)
    print("Man - I have a job for you.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.I'm listening.")
    print("2.No i'm fine.")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one_one()
    elif choice == "2":
        Thieftwo_one_two()

def Thieftwo_two():
    print("You - Want a drink?")
    time.sleep(1)
    print("Man - Yeah, sure.")
    time.sleep(1)
    print("You buy the man a drink and he turns to you.")
    time.sleep(1)
    print("Man - I have a job for you.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.I'm listening.")
    print("2.No i'm fine.")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one_one()
    elif choice == "2":
        Thieftwo_two_two()

def Thieftwo_three():
    print("You - What's it to you?")
    time.sleep(1)
    print("Man - I wouldn't speak to a man, who will give you 50 gold like that.")
    time.sleep(3)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.What will I have to do?")
    print("2.I don't care.")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one_one()
    elif choice == "2":
        Thieftwo_one_two_two()

def Thiefthree_one():
    print("You - What do you want?")
    time.sleep(1)
    print("Man - I have a business propossal.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.I'm listening.")
    print("2.No i'm fine.")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one_one()
    elif choice == "2":
        Thieftwo_two_two()

def Thiefthree_two():
    print("Man - Excuse me, I have a business proposal.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.I'm listening.")
    print("2.I'm fine.")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one_one()
    elif choice == "2":
        Thieftwo_two_two()

def Thiefone_one_one():
    print("You - Someone like me?")
    time.sleep(1)
    print("Man - Yes, I need you to do a job for me.")
    input("Press enter to continue.")
    print("1.I'm listening.")
    print("2.I'm fine.")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one_one()
    elif choice == "2":
        Thieftwo_one_two()

def Thieftwo_one_one():
    print("Man - I need you to get something for me.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Okay, what do you want getting?")
    print("2.From who?")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one_one_one()
    elif choice == "2":
        Thieftwo_one_one_two()

def Thieftwo_one_two():
    print("You - No I'm fine thanks.")
    time.sleep(1)
    print("Man - There's 50 gold for you.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Sure, I'll do it.")
    print("2.I don't care.")
    choice = input(">>>")
    if choice == "1":
        Thieftwo_one_one()
    elif choice == "2":
        Thieftwo_one_two()

def Thieftwo_one_two():
    print("Man - Your loss.")
    time.sleep(1)
    input("Press enter to continue.")
    print("1.Ask him to increase the price.")
    print("2.I changed my mind.")
    choice = input(">>>")
    if choice == "1":
        print("Man - No but here is what I want you to do.")
        time.sleep(1)
        Thieftwo_one_one()
    elif choice == "2":
        print("You - I changed my mind.")
        time.sleep(1)
        print("Man - Make your mind up.")
        time.sleep(1)
        Thieftwo_one_one()

def Thieftwo_one_one_one():
    print("Man - I would like you to steal the king's crown.")
    time.sleep(1)
    print("You - Consider it done.")
    print("Thank you for testing out the first release!")
    input("Press enter to continue.")
    Thiefleave()

def Thieftwo_one_one_two():
    print("Man: The king.")
    time.sleep(1)
    Thieftwo_one_one_one()

def Thiefleave():
    credit()

#Medic

    
#Warrior
def Warriorintro():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("You are training in the training")
    print("yard, when you notice the king")
    print("looking at you. He beckons you.")
    time.sleep(5)
    print("King Sean - I have a problem. Some little street rat, stole my crown from me.")
    time.sleep(1)
    print("King Sean - And I need you to retreive it.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Spit in his face.")
    print("2.Follow orders.")
    choice = input(">>>")
    if choice == "1":
        wone()
    elif choice == "2":
        wtwo()

def wone():
    print("You spit at the king and two guards retrain you.")
    time.sleep(1)
    print("King Sean - How dare you! Throw him in the dungeon.")
    time.sleep(1)
    input("Press enter to continue.")
    wone_d()

def wtwo():
    print("You - I will find that crown at all costs.")
    time.sleep(1)
    print("King Sean - And if you don't I'll have your head.")
    time.sleep(1)
    input("Press enter to continue.")
    print("Where will you start your search?")
    print("1.The inn.")
    print("2.The blacksmith.")
    choice = input(">>>")
    if choice == "1":
        wtwo_inn()
    elif choice == "2":
        wtwo_bs()
    
    
def wone_d():
    print("You have been in this cold cell for 3 hours now.")
    time.sleep(1)
    print("You must escape this place to avoid execution.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Try to open the window.")
    print("2.Stab the guard with the metal on the floor.")
    choice = input(">>>")
    if choice == "1":
        wone_d_one()
    elif choice == "2":
        wone_d_two

def wone_d_one():
    print("You successfully pick the lock, with a piece of metal you found on the floor")
    print("and you climb out.")
    time.sleep(1)
    print("3 days ago.")
    input("Press enter to continue.")
    openFileT()

def wone_d_two():
    print("You lure the guard over and slit his throat")
    print("with the metal.")
    time.sleep(2)
    print("You grab his keys and climb out the window.")
    time.sleep(1)
    print("3 days ago.")
    input("Press enter to continue.")
    wopenFileT()

def wtwo_inn():
    print("You are here to find the theif no one else.")
    time.sleep(1)
    print("Man - How's  my favourite buddy?")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Ask him what the hell is he on about.")
    print("2.Yeah, I know who you are.")
    choice = input(">>>")
    if choice == "1":
        wtwo_inn_man()
        print("You - What the hell are you on about?")
        time.sleep(1)
        
    elif choice == "2":
        print("You - Yeah I exactly know who you are... Not a clue. Fill me in.")
        time.sleep(3)
        wtwo_inn_man()

def wtwo_inn_man():
    print("Man - You really don't remember do you?")
    time.sleep(1)
    print("You - No I don't.")
    time.sleep(1)
    print("Man well this is how it went.")
    input("Press enter to continue.")
    credit()

def wtwo_bs():
    print("You are here to find the theif no one else.")
    time.sleep(1)
    print("Adam - Hey, how you doing?")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Cut the chat. I'm here by order of the crown.")
    print("2.Good thanks Adam.")
    print("3.Move out the way.")
    choice = input(">>>")
    if choice == "1":
        wtwo_bs_one()
    elif choice == "2":
        wtwo_bs_two_o()
    elif choice == "3":
        two_bs_three()

def wtwo_bs_one():
    print("You - Cut the Chat, Adam. I'm here by order of the crown.")
    print("Adam - Okay... What happened.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.None of your business.")
    print("2.I'm the one asking the questions here.")
    choice = input(">>>")
    if choice == "1":
        wtwo_bs_one_one()
    elif choice == "2":
        wtwo_bs_two()

def wtwo_bs_two():
    print("Adam - Okay, what's the problem.")
    input("Press enter to continue.")
    print("What will you do?")
    print("1.The crown has been stolen.")
    print("2.I'm the one asking the questions here.")
    print("3.None of your business.")
    choice = input(">>>")
    if choice == "1":
        wtwo_bs_two_one()
    elif choice == "2":
        wtwo_bs_two()
    elif choice == "3":
        wtwo_bs_one_one()

def wtwo_bs_two_one():
    print("You - The crown has been stolen. Can I go inside?")
    time.sleep(1)
    print("Adam - Sure.")
    time.sleep(1)
    print("You will now go inside.")
    time.sleep(1)
    input("Press enter to continue.")
    wtwo_bs_i()
    
def wtwo_bs_three():
    print("You - Move now!")
    time.sleep(1)
    print("You push Adam to the floor.")
    time.sleep(1)
    print("Adam - What was that for?")
    time.sleep(1)
    print("You will now go inside.")
    time.sleep(1)
    input("Press enter to continue.")
    wtwo_bs_i()

def wtwo_bs_one_one():
    print("You - None of your business.")
    time.sleep(1)
    print("Adam - What's your problem?")
    time.sleep(1)
    print("You - I'm here for work.")
    time.sleep(1)
    print("You will now go inside.")
    time.sleep(1)
    input("Press enter to continue.")
    wtwo_bs_i()

def wtwo_bs_two():
    print("You - I'm the one asking the questions here.")
    time.sleep(1)
    print("Adam - Okay. Want to go inside?")
    time.sleep(1)
    print("You - Yes.")
    time.sleep(1)
    input("Press enter to continue.")
    wtwo_bs_i()

def wtwo_bs_two_o():
    print("You - I good thanks Adam.")
    time.sleep(1)
    print("Adam - Want to come inside?")
    time.sleep(1)
    print("You - Sure.")
    time.sleep(1)
    print("You will now go inside.")
    time.sleep(1)
    input("Press enter to continue.")
    wtwo_bs_i

def wtwo_bs_i():
    print("As you look around you notice something sparkling in the corner.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Check it out.")
    print("2.Ask Adam a question.")
    choice = input(">>>")
    if choice == "1":
        wbs_i_one()
    elif choice == "3":
        wbs_i_three()

def wbs_i_one():
    print("Adam - Don't go over there!")
    time.sleep(1)
    print("You - Why not?")
    time.sleep(1)
    print("Adam - It's your birthday presant.")
    time.sleep(1)
    print("You - Yeah, right.")
    time.sleep(1)
    print("When you get there you find a necklace with your name inscribed on it.")
    time.sleep(1)
    print("Adam - Well done.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Ask about it.")
    print("2.Ask Adam a question.")
    choice = input(">>>")
    if choice == "1":
        wbs_i_one_one()
    elif choice == "2":
        wbs_i_one_two()

def wbs_i_one_one():
    print("You - How much was it?")
    time.sleep(1)
    print("Adam - 75 gold.")
    time.sleep(1)
    print("You - Thank you. But I got to carry on searching.")
    time.sleep(1)
    print("You will now return to the middle of the room.")
    input("Press enter to continue.")
    wbs_i_one_t1()

def wbs_i_one_t1():
    print("Adam - Now your birthday is ruined.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Ask Adam a question.")
    choice = input(">>>")
    if choice == "1":
        wbs_i_three()

def wbs_i_three():
    print("You - May I ask you a question?")
    time.sleep(1)
    print("Adam - Ask away.")
    time.sleep(1)
    input("Press enter to continue.")
    print("What will you do?")
    print("1.Any suspicious packages come here lately?")
    print("2.Have you received a large number of gold recently?")
    print("3.Go back into the middle.")
    print("4.Search the inn.")
    choice = input(">>>")
    if choice == "1":
        print("You: Any supicious packages come here lately?")
        time.sleep(1)
        print("Adam: Not that I know of.")
        time.sleep(1)
        print("What will you ask next?")
        input("Press enter to continue.")
        wbs_i_three()
    elif choice == "2":
        print("You - Have you received a large number of gold recently?")
        time.sleep(1)
        print("Adam - No.")
        time.sleep(1)
        print("You - Are you sure?")
        time.sleep(1)
        print("Adam - I would know about it if there was.")
        time.sleep(1)
        print("What will you ask next?")
        input("Press enter to continue.")
        wbs_i_three()
    elif choice == "3":
        wtwo_bs_i()
    elif choice == "4":
        print("You will now search the inn.")
        input("Press enter to continue.")
        wtwo_inn()

## Credits
def credit():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    time.sleep(3)
    print("Thankyou for playing!")
    print("+--------------------------------+")
    time.sleep(1)
    print("Classes")
    time.sleep(0.75)
    print("Benjamin Keogh")
    time.sleep(0.75)
    print("Brandon Davis")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("Gender and Role configuration")
    time.sleep(0.75)
    print("Benjamin Keogh")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("Character Names")
    time.sleep(0.75)
    print("Benjamin Keogh")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("Python Basic Code")
    time.sleep(0.75)
    print("Benjamin Keogh")
    time.sleep(0.75)
    print("Brandon Davis")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("Python Advanced Code")
    time.sleep(0.75)
    print("Benjamin Keogh")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("Storyline")
    time.sleep(0.75)
    print("Brandon Davis")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("Character roles")
    time.sleep(0.75)
    print("Brandon Davis")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("File Merging and Configuration")
    time.sleep(0.75)
    print("Benjamin Keogh")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("Choice answers")
    time.sleep(0.75)
    print("Brandon Davis")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("Character Speech")
    time.sleep(0.75)
    print("Brandon Davis")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("BETA Testing")
    time.sleep(0.75)
    print("Benjamin Keogh")
    time.sleep(0.75)
    print("Brandon Davis")
    time.sleep(0.75)
    print("Adam Hill")
    time.sleep(0.75)
    print("MORE TO COME")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("ALPHA Testers")
    time.sleep(0.75)
    print("NOT IN ALPHA AS OF NOW")
    time.sleep(0.75)
    print()
        
intro()
