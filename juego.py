def cuarto_uno():

	print("Estás en la habitación número uno. Tienes a la izquierda una puerta y a la derecha otra. \nPuedes intentar abrirlas")
	
	salir = True

	while salir:
		move = input("Que vas a hacer? ")
		if move == "izquierda":
			print("No tienes los objetos necesarios para salir.")
			continue
		elif move == "derecha":
			salir = False
			cuarto_dos()
		else:
			print("no entiendo lo que quieres hacer")
			continue

def cuarto_dos():

	print("Estás en la habitación número dos. Aquí hay tres puertas")
	print("Tienes una puerta al frente, una a la izquierda y otra a la derecha. \nPuedes intentar abrirlas")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "abrir izquierda":
			salir = True
			cuarto_uno()
		elif move == "abrir derecha":
			salir = True
			cuarto_tres()
		elif move == "abrir frente":
			salir = True
			cuarto_cinco()
		else:
			print("no entiendo lo que quieres hacer")
			continue

def cuarto_tres():

	print("Estás en la habitación número tres. Aquí hay dos puertas")
	print("Tienes una puerta a la izquierda y otra a la derecha. \nPuedes intentar abrirlas")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "abrir izquierda":
			salir = True
			cuarto_dos()
		elif move == "abrir derecha":
			salir = True
			cuarto_cuatro()
		else:
			print("no entiendo lo que quieres hacer")
			continue

def cuarto_cuatro():

	print("Estás en la habitación número cuatro. Aquí hay dos puertas")
	print("Tienes una puerta a la izquierda y otra a la derecha. \nPuedes intentar abrirlas")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "abrir izquierda":
			salir = True
			cuarto_cinco()
		elif move == "abrir derecha":
			salir = True
			cuarto_tres()
		else:
			print("no entiendo lo que quieres hacer")
			continue

def cuarto_cinco():

	print("Estás en la habitación número cinco. Aquí hay tres puertas")
	print("Tienes una puerta al frente, una a la izquierda y otra a la derecha. \nPuedes intentar abrirlas")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "abrir izquierda":
			salir = True
			cuarto_seis()
		elif move == "abrir derecha":
			salir = True
			cuarto_cuatro()
		elif move == "abrir frente":
			salir = True
			cuarto_dos()
		else:
			print("no entiendo lo que quieres hacer")
			continue

def cuarto_seis():

	print("Estás en la habitación número seis. Aquí hay una puerta")
	print("Tienes una puerta a la derecha. \nPuedes intentar abrirla.")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "abrir izquierda":
			salir = True
			print("Has abierto la puerta al infinito. Tu cuerpo flotará en el espacio por toda la eternidad.")
		elif move == "abrir derecha":
			salir = True
			cuarto_cinco()
		else:
			print("no entiendo lo que quieres hacer")
			continue

cuarto_uno()