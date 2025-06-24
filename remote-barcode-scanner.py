import pyautogui
import json
import socket
import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        # When the program is executed as .exe
        return os.path.dirname(sys.executable)
    else:
        # When the program is executen as .py
        return os.path.dirname(os.path.abspath(__file__))

def loadConfig():
	config_path = os.path.join(get_base_path(), 'config.json')
	with open(config_path, 'r') as configFile:
		configData = json.load(configFile)

	print("Configuración: ")
	print(configData)
	return configData

while True: 
	try:
		configData = loadConfig()
		host = configData["ip"]
		port = int(configData["port"])
		EOF = "EOF"
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind((host, port))
		server_socket.listen(1)
		print(f'Servidor escuchando en {host}:{port}')

		while True:
			data = None
			client_socket, client_address = server_socket.accept()
			print(f'Conexión aceptada de {client_address}')
			while True:
				message = client_socket.recv(1024).decode('utf-8')
				print(f"Received: {message}")
				if message:
					pyautogui.write(message, 0.01)
					pyautogui.press("enter")
				else:
					print('No se recibió ningún dato.')

				client_socket.close()
				print(f'Conexión cerrada con {client_address}')
				break
	except Exception as e:
		print(f"Ocurrió un error: {e}")