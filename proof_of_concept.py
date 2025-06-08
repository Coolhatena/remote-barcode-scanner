import pyautogui
import time

print("El texto se escribirá en 5 segundos...")
time.sleep(5)
pyautogui.write("Hola, esto fue escrito por Python.")
pyautogui.press("enter")