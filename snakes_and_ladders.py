import random
import time

max_value = 100

snake_heads = [32, 34, 48, 62, 88, 95, 97]
snake_tails = [10, 6, 26, 18, 24, 56, 78]

ladder_bottom = [1, 4, 8, 21, 28, 50, 71, 80]
ladder_top = [38, 14, 30, 42, 76, 67, 92, 99]

pos_1 = 0
pos_2 = 0

while pos_1 != max_value and pos_2 != max_value:
    print('')
    input("Player 1, press enter to roll the die.")
    die_roll_1 = random.randint(1, 6)
    pos_1 = pos_1 + die_roll_1
    print('')
    print("You rolled a", die_roll_1, "!")
    print("You are now at square:", pos_1)
    print('')

    if pos_1 in snake_heads:
        snake_index = snake_heads.index(pos_1)
        pos_1 = snake_tails[snake_index]
        print("You got bit by a snake! You are now at square:", pos_1)
        print('')
        
    elif pos_1 in ladder_bottom:
        ladder_index = ladder_bottom.index(pos_1)
        pos_1 = ladder_top[ladder_index]
        print("You climbed a ladder! You are now at square:", pos_1)
        print('')

    elif pos_1 > max_value:
        pos_1 = pos_1 - die_roll_1
        print("You went over 100! You're back at square:", pos_1)
        print('')

    time.sleep(1)

    if pos_1 == max_value:
        for i in range(11):
            print("\ | | / ")
            print(" -YOU WIN- ")
            print("/ | | \\")
            time.sleep(0.5)
            print(" ")
            print(" YOU WIN ")
            print(" ")
            time.sleep(0.5)
        break

    if pos_1 != max_value:
        print('')
        input("Player 2, press enter to roll the die.")
        die_roll_2 = random.randint(1, 6)
        pos_2 = pos_2 + die_roll_2
        print('')
        print("You rolled a", die_roll_2, "!")
        print("You are now at square:", pos_2)
        print('')

        if pos_2 in snake_heads:
            snake_index = snake_heads.index(pos_2)
            pos_2 = snake_tails[snake_index]
            print("You got bit by a snake! You are now at square:", pos_2)
            print('')

        elif pos_2 in ladder_bottom:
            ladder_index = ladder_bottom.index(pos_2)
            pos_2 = ladder_top[ladder_index]
            print("You climbed a ladder! You are now at square:", pos_2)
            print('')

        elif pos_2 > max_value:
            pos_2 = pos_2 - die_roll_2
            print("You went over 100! You're back at square:", pos_2)
            print('')
            

        time.sleep(1)

        if pos_2 == max_value:
            for i in range(11):
                print("\ | | / ")
                print(" -YOU WIN- ")
                print("/ | | \\")
                time.sleep(0.5)
                print(" ")
                print(" YOU WIN ")
                print(" ")
                time.sleep(0.5)
            break
