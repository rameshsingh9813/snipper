import pyautogui as pag
import time
import os

# variable declaration
ss_location = str(input("enter the location to save image: "))
ss_coordinate = (345,85,855,535)
print(type(ss_location),type(ss_coordinate))
sleep_time = 0.2
ss_t_c = (10, 50)  # screenshot taking coordinate
p_t_c = (0, 10)  # program terminate coordinate
os.chdir(ss_location)


# screenshot taker function
def take_ss(count):
    ss = pag.screenshot(region=ss_coordinate)
    ss.save(rf'screenshot{count}.png')
    print(rf'screenshot{count}.png')


# time decider for the different action
def time_definer_for_screenshot():
    updator = 0
    insideif = 0
    insideelif_2 = 0
    while True:
        time.sleep(sleep_time)
        x, y = pag.position()
        if x < ss_t_c[0] and y > ss_t_c[1]:
            insideif += 1
            if insideif < 2:
                take_ss(updator)
                updator += 1

        elif y < p_t_c[1]:
            return False

        else:
            insideif = 0
            insideelif_2 += 0


time_definer_for_screenshot()
