import time
import random
import keyboard
def qte():
    # Generate a random number between 1 and 4
    target_number = str(random.randint(1, 4))
    print(f"Type the number: {target_number}")
    start_time = time.time()
    typed_number = ""
    # Collect keystrokes
    while time.time() - start_time < 5:  # 5 seconds time limit
        if keyboard.is_pressed(target_number):
            typed_number = target_number
            break
    # Check if the input matches the target number
    if typed_number == target_number:
        print("Success! You typed the correct number in time.")
    else:
        print(f"Too late or incorrect! The correct number was {target_number}.")
qte()