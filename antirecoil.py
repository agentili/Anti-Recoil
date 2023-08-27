
import random
import time

import keyboard
import mouse
from termcolor import colored

## Configuration
# Set the horizontal limit: 5 means a maximum of 5 pixels to the left or to the right every shot
horizontal_range = 5
# Set the minimum and maximum amount of pixels to move the mouse every shot
min_vertical = 8
max_vertical = 10
# Set the minimum and maximum amount of time in seconds to wait until moving the mouse again
min_firerate = 0.03
max_firerate = 0.05
# Set the toggle button
toggle_button = 'end'
# Set whether the anti-recoil is enabled by default
enabled = False

# Some prints for startup
print("Anti-recoil script started!")
if enabled:
    print("Currently ENABLED")
else:
    print("Currently DISABLED")

last_state = False
while True:
    key_down = keyboard.is_pressed(toggle_button)
    # If the toggle button is pressed, toggle the enabled value and print
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("Anti-recoil", colored('****ENABLED****', 'green'))
            else:
                print("Anti-recoil", colored('DISABLED', 'red'))

    if mouse.is_pressed() and enabled:
        if count == 0:
            keyboard.press_and_release('Alt')
            count = 1

        # Offsets are generated every shot between the min and max config settings
        offset_const = 1000
        horizontal_offset = random.randrange(-horizontal_range * offset_const, horizontal_range * offset_const, 1) / offset_const
        vertical_offset = random.randrange(min_vertical * offset_const, max_vertical * offset_const, 1) / offset_const

        # print("Move: " , horizontal_offset , " " , vertical_offset)

        # Move the mouse with these offsets
        # win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))
        mouse.move(int(horizontal_offset), int(vertical_offset), False)

    # Delay for the while loop
    time.sleep(0.01)