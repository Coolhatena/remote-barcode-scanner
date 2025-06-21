import pyautogui
import time

message = input('Texto a escribir: ')
print("El texto se escribirá en 5 segundos...")
time.sleep(5)
pyautogui.write(message)
pyautogui.press("enter") # Needed to submit the input text, or put input as a row in a file
