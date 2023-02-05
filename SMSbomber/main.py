import pyautogui
import time

message = 50  # Number of sms you want to send
text = 'hello sweet hart :)'  # The text you want to send

time.sleep(3)
while message>0:
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        message = message - 1


