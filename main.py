import pyautogui
import time
while True:
    for i in range(7):
        if i==0:
            pyautogui.typewrite(" Hello ")
            pyautogui.press('enter')
        elif i==1:
            pyautogui.typewrite(" HellO")
            pyautogui.press('enter')
        elif i==2:
            pyautogui.typewrite(" Surprise for you. ")
            pyautogui.press('enter')
        elif i==3:
            pyautogui.typewrite(" Happy Birthday.")
            pyautogui.press('enter')
        elif i==4:
            pyautogui.typewrite(" Happy Birthday.")
            pyautogui.press('enter')
        elif i==5:
            pyautogui.typewrite("Happy Birthday.")
            pyautogui.press('enter')
        elif i==6:
            pyautogui.typewrite("Happy Birthday.")
            pyautogui.press('enter')
        elif i==7:
            pyautogui.typewrite("Happy Birthday."
                                "Happy Birthday."
                                "Happy Birthday."
                                "Happy Birthday."
                                " Happy Birthday."
                                "Happy Birthday.")

            pyautogui.press('enter')
        else:
            continue
