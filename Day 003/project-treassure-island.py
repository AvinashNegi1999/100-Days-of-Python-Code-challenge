# Treasure Island Game
# A text-based adventure game with ASCII art and input validation.

print(''' 
*******************************************************************************
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

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("Do you want to go left or right? L or R: ").lower()

if direction == "l":
    choice = input("Do you want to swim or wait? S or W: ").lower()
    
    if choice == "w":
        door = input("Which door do you choose? Red, Blue or Yellow? R or B or Y: ").lower()
        
        if door == "y":
            print('''
CONGRATULATIONS, YOU FOUND THE TREASURE!

             __________
            /\\____;;___\\
           | /         /
           `. ())oo() .
            |\\(%()*^^()^\\
           %| |-%-------|
          % \\ | %  ))   |
          %  \\|%________|
            __||__||__||
           (__)__)__)__)
''')
        elif door == "r":
            print('''
You opened the red door and got burned by fire.

              (  .      )
          )           (              )
                .  '   .   '  .  '  .
       (    , )       (.   )  (   ',    )
        .' ) ( . )    ,  ( ,     )   ( .
     ). , ( .   (  ) ( , ')  .' (  ,    )
    (_,) . ), ) _) _,')  (, ) '. )  ,. (' )

GAME OVER.
''')
        elif door == "b":
            print('''
You opened the blue door and were eaten by beasts.

      ,     ,      
     (\\____/)     
      (_oo_)      
        (O)       
      __||__     \\) 
   []/______\\[] /
   / \\______/ \\
  /    /__\\    
 (\\   /____\\

GAME OVER.
''')
        else:
            print("Invalid door choice. Game Over.")
    elif choice == "s":
        print('''
You chose to swim and were attacked by trout.

        ~ ~ ~ ~ ~
     ><(((*>    ><(((*>    ><(((*>
        ~ ~ ~ ~ ~

GAME OVER.
''')
    else:
        print("Invalid action. Game Over.")
elif direction == "r":
    print('''
You went right and fell into a hole.

         \\  |  /
           .-'-. 
        -- /   \\ --
           \\___/
          ( . . )
          (  -  )
         _(   )_
        /       \\

GAME OVER.
''')
else:
    print("Invalid direction. Game Over.")
