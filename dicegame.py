import random
import time

min = 1
max = 6

roll_again = 'yes'
yes_options =['yes', "y", "Y", "Yes"]
if  roll_again in yes_options:
    print("Rolling The Dices...")
    time.sleep(3)
    print('The values are: ')
    print(random.randrange(min, max + 1))
    print(random.randrange(min, max + 1))

    roll_again = input("Repeat? ")

else:
    print("Invalid")