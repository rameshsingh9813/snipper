import pyautogui as pag
import time
import os
import pytesseract.pytesseract



# variable declaration
link=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd=link
screenres_x, screenres_y=pag.size()
user_location = str(input("enter the location to save image: "))
os.chdir(user_location)

 # screenshot taker function
def takeimage(count):
    myScreenshot = pag.screenshot(region=(345,85,855,535))
    myScreenshot.save(rf'screenshot{count}.png')
    text = pytesseract.image_to_string(rf'screenshot{count}.png')
    lists = text.split(' ')
    os.rename(rf'screenshot{count}.png', f'{lists[1]}+.png')
    print(lists[5])


# time decider for the differnt difernt action
def time_definer_for_screenshot():
    updator=0
    insideif=0
    insideelif_1=0
    insideelif_2=0
    folder_count=1
    while True:
        time.sleep(0.2)
        x, y = pag.position()
        print(x,y)
        if x<10 and y>50:
            insideif+=1
            if insideif<2:
                takeimage(updator)
                updator += 1

        elif x>pag.size().width-30 and y<int(pag.size().height/2):
            insideelif_1+=1
            if insideelif_1<2:
                os.mkdir(f"Design_{folder_count}")
                os.chdir(f"Design_{folder_count}")
                folder_count+=1
                time.sleep(0.2)

        elif x>pag.size().width-30 and y>int(pag.size().height/2):
            insideelif_2+=1
            if insideelif_2<2:
                # os.mkdir(f"Design_{folder_count}")
                os.chdir("..")

        elif y<10:
            return False

        else:
            insideif=0
            insideelif_1=0
            insideelif_2 += 0


time_definer_for_screenshot()



print("i am good")
print("ohh no i am a good man")