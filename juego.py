"""el juego se desarrolla en seis habitaciones de las que el jugador puede entrar y salir de acuerdo
a las indicaciones. Para terminar el juego debera salir por la puerta indicada teniendo en su poder los
objetos correctos. Cada habitacion esta representada por una funcion"""

def cuarto_uno():
    """funcion del primer cuarto. En esta habitacion comienza el juego y tambien esta la puerta de salida"""

    print("Estás en la habitación número uno. Tienes a la izquierda una puerta y a la derecha otra. \nPuedes intentar las")
    salir = True

    while salir:
        move = input("Que vas a hacer? ")
        if move == "izquierda":
            print("No tienes los objetos necesarios para salir.")
        elif move == "derecha":
            salir = False
            cuarto_dos()
        else:
            print("no entiendo lo que quieres hacer")
            continue

def cuarto_dos():

    print("Estás en la habitación número dos. Aquí hay tres puertas")
    print("Tienes una puerta al frente, una a la izquierda y otra a la derecha. \nPuedes intentar las")
    salir = False
    while not salir:
        move = input("Que vas a hacer? ")
        if move == "izquierda":
            salir = True
            cuarto_uno()
        elif move == "derecha":
            salir = True
            cuarto_tres()
        elif move == "frente":
            salir = True
            cuarto_cinco()
        else:
            print("no entiendo lo que quieres hacer")
            continue

def cuarto_tres():

	print("Estás en la habitación número tres. Aquí hay dos puertas")
	print("Tienes una puerta a la izquierda y otra a la derecha. \nPuedes intentar las")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "izquierda":
			salir = True
			cuarto_dos()
		elif move == "derecha":
			salir = True
			cuarto_cuatro()
		else:
			print("no entiendo lo que quieres hacer")
			continue

def cuarto_cuatro():

	print("Estás en la habitación número cuatro. Aquí hay dos puertas")
	print("Tienes una puerta a la izquierda y otra a laderecha. \nPuedes intentar las")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "izquierda":
			salir = True
			cuarto_cinco()
		elif move == "derecha":
			salir = True
			cuarto_tres()
		else:
			print("no entiendo lo que quieres hacer")
			continue

def cuarto_cinco():

	print("Estás en la habitación número cinco. Aquí hay tres puertas")
	print("Tienes una puerta al frente, una a la izquierda y otra a la derecha. \nPuedes intentar abrir las")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "izquierda":
			salir = True
			cuarto_seis()
		elif move == "derecha":
			salir = True
			cuarto_cuatro()
		elif move == "frente":
			salir = True
			cuarto_dos()
		else:
			print("no entiendo lo que quieres hacer")
			continue

def cuarto_seis():

	print("Estás en la habitación número seis. Aquí hay una puerta")
	print("Tienes una puerta a la derecha. \nPuedes intentar la.")
	salir = False
	while not salir:
		move = input("Que vas a hacer? ")
		if move == "izquierda":
			salir = True
			print("Has abierto la puerta al infinito. Tu cuerpo flotará en el espacio por toda la eternidad.")
		elif move == "derecha":
			salir = True
			cuarto_cinco()
		else:
			print("no entiendo lo que quieres hacer")
			continue

cuarto_uno()