import time

def countdown(number):
    while number >= 0:
        if number > 0:
            print(f"{number} SECOND(S)!")
        else:
            print("HAPPY NEW YEAR!")
        number -= 1

def countdown_with_sleep(number):
    while number >= 0:
        if number > 0:
            print(f"{number} SECOND(S)!")
        else:
            print("HAPPY NEW YEAR!")
        number -= 1
        time.sleep(1)
        