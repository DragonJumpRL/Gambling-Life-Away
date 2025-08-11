#Program for slots

#array defining different slot options
init python:
    slot1 = ["grave", "cherry", "drink", "bell", "bar", "coin", "seven", "dice", "chest", "demon"]
    sweights = [2, 35, 20, 15, 13, 10, 7, 5, 4, 2 ]
    
    
    




#Variables for slots
default s_bet = 0

#images used
image grave = "images/slots/grave.png"
image cherry = "images/slots/cherry.png"
image drink = "images/slots/drink.png"
image bell = "images/slots/bell.png"
image bar = "images/slots/bar.png"
image coin = "images/slots/coin.png"
image seven = "images/slots/seven.png"
image dice = "images/slots/dice"
image chest = "images/slots/chest"
image demon = "images/slots/demon"

#screen for slot display
screen slots_display():
    frame:
        xsize 1000
        ysize 600
    







#Slot dialogue and choices
label slots_machine:
    scene bg casino_floor
    
    "You arrive at bustling area of slot machines and find and empty one to play"

    menu:
        "What would you like to do"

        "Roll some slots":
            jump slots_bet
        
        "Return to the casino floor":
            jump casino_hub


#slot betting system
label slots_bet:
    $ s_bet = 0
    # If you’re broke, bounce back.
    if money <= 0:
        "You check your Player Card... 0 credits. No money, no fun."
        jump casino_hub

    # If you don’t have the minimum (100), go back to the table.
    if money < 100:
        "You pat your pockets... not enough for the minimum play."
        jump slots_machine

    menu:
        "Machine: Insert money to play"

        "100" if money >= 100:
            $ s_bet = 100
            $ money -= s_bet
            "You put [s_bet] credits into the machine."
            jump play_slots

        "250" if money >= 250:
            $ s_bet = 250
            $ money -= s_bet
            "You put [s_bet] credits into the machine."
            jump play_slots

        "500" if money >= 500:
            $ s_bet = 500
            $ money -= s_bet
            "You put [s_bet] credits into the machine."
            jump play_slots

        "1000" if money >= 1000:
            $ s_bet = 1000
            $ money -= s_bet
            "You put [s_bet] credits into the machine."
            jump play_slots

        "Never mind (back)":
            jump slots_machine 

#Slot rolling
label play_slots:
    $ reel1 = random.choices(slot1, weights=sweights, k=1)[0]
    $ reel2 = random.choices(slot1, weights=sweights, k=1)[0]
    $ reel3 = random.choices(slot1, weights=sweights, k=1)[0]
    "The reels show: [reel1] | [reel2] | [reel3]"
    if reel1 == reel2 == reel3:
        $ money += s_bet*1.5

    if reel1 == reel2:
        $ money += s_bet
    elif reel2 == reel3:
        $ money += s_bet

    pause 3.0
    jump slots_bet



   



    