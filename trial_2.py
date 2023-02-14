# import pyautogui as pag
# import time
# import os
#
#
# def all_in_one(loc,cordinate):
#     # variable declaration
#     ss_location = str(input("enter the location to save image: "))
#     ss_coordinate = (345, 85, 855, 535)
#     sleep_time = 0.2
#     ss_t_c = (10, 50)  # screenshot taking coordinate
#     p_t_c = (0, 10)  # program terminate coordinate
#     os.chdir(ss_location)
#
#
#     # screenshot taker function
#     def take_ss(count):
#         ss = pag.screenshot(region=ss_coordinate)
#         ss.save(rf'screenshot{count}.png')
#         print(rf'screenshot{count}.png')
#
#
#     # time decider for the different action
#     def time_definer_for_screenshot():
#         updator = 0
#         insideif = 0
#         insideelif_2 = 0
#         while True:
#             time.sleep(sleep_time)
#             x, y = pag.position()
#             if x < ss_t_c[0] and y > ss_t_c[1]:
#                 insideif += 1
#                 if insideif < 2:
#                     take_ss(updator)
#                     updator += 1
#
#             elif y < p_t_c[1]:
#                 return False
#
#             else:
#                 insideif = 0
#                 insideelif_2 += 0
#
#
#     time_definer_for_screenshot()


import pyautogui as pag
print(pag.size().height)

print((855/1366)*1920)
print((535/768)*1080)