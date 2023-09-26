"""el juego se desarrolla en seis habitaciones de las que el jugador 
puede entrar y salir de acuerdo a las indicaciones. 
Para terminar el juego debera salir por la puerta indicada 
teniendo en su poder los objetos correctos. 
Cada habitacion esta representada por una funcion"""

mochila = ["", ""]
objetos = [
    "Destornillador", "Mancuerna", "Pelota", "Llave", "Termo", "Celular", 
    "Manzana", "Billetera", "Mate", "Bicicleta", "Campera", "Radio"]

def cuarto_uno():
    """funcion del primer cuarto. En esta habitacion comienza 
    el juego y tambien esta la puerta de salida"""

    print("\nEstás en la habitación número uno. Tienes"\
          " a la izquierda una puerta y a la derecha otra. \nPuedes intentar abrirlas")
    print(f"En la habitación hay dos objetos que tal vez te sirvan ({objetos[0]} y {objetos[1]}). ")
    print("Puedes guardarlos en tu mochila de a uno y solo puedes llevar dos objetos.")
    salir = True

    while salir:
        move = input("Que vas a hacer? ")
        if move == "izquierda":
            if "Termo" in mochila and "Mate" in mochila:
                print("Lo has logrado. Puedes salir de la casa!")
                exit()
            else:
                print("No tienes los objetos necesarios para salir.")
        elif move == "derecha":
            salir = False
            cuarto_dos()
        elif move == objetos[0]:
            mochila[0], mochila[1], objetos[0] = objetos[0], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        elif move == objetos[1]:
            mochila[0], mochila[1], objetos[1] = objetos[1], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        else:
            print("no entiendo lo que quieres hacer")
            continue

def cuarto_dos():

    print("\nEstás en la habitación número dos. Aquí hay tres puertas")
    print("Tienes una puerta al frente, una a la izquierda y otra a la derecha." \
          "\nPuedes intentar abrirlas")
    print(f"En la habitación hay dos objetos que tal vez te sirvan ({objetos[2]} y {objetos[3]}). ")
    print("Puedes guardarlos en tu mochila de a uno y solo puedes llevar dos objetos.")

    salir = False
    while not salir:
        move = input("Que vas a hacer?  ")
        if move == "izquierda":
            salir = True
            cuarto_uno()
        elif move == "derecha":
            salir = True
            cuarto_tres()
        elif move == "frente":
            salir = True
            cuarto_cinco()
        elif move == objetos[2]:
            mochila[0], mochila[1], objetos[2] = objetos[2], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        elif move == objetos[3]:
            mochila[0], mochila[1], objetos[3] = objetos[3], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        else:
            print("no entiendo lo que quieres hacer")
            continue

def cuarto_tres():

    print("\nEstás en la habitación número tres. Aquí hay dos puertas")
    print("Tienes una puerta a la izquierda y otra a la derecha. \nPuedes intentar abrirlas")
    print(f"En la habitación hay dos objetos que tal vez te sirvan ({objetos[4]} y {objetos[5]}). ")
    print("Puedes guardarlos en tu mochila de a uno y solo puedes llevar dos objetos.")

    salir = False
    while not salir:
        move = input("Que vas a hacer? ")
        if move == "izquierda":
            salir = True
            cuarto_dos()
        elif move == "derecha":
            salir = True
            cuarto_cuatro()
        elif move == objetos[4]:
            mochila[0], mochila[1], objetos[4] = objetos[4], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        elif move == objetos[5]:
            mochila[0], mochila[1], objetos[5] = objetos[5], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        else:
            print("no entiendo lo que quieres hacer")
            continue

def cuarto_cuatro():

    print("\nEstás en la habitación número cuatro. Aquí hay dos puertas")
    print("Tienes una puerta a la izquierda y otra a laderecha. \nPuedes intentar abrirlas")
    print(f"En la habitación hay dos objetos que tal vez te sirvan ({objetos[6]} y {objetos[7]}). ")
    print("Puedes guardarlos en tu mochila de a uno y solo puedes llevar dos objetos.")

    salir = False
    while not salir:
        move = input("Que vas a hacer? ")
        if move == "izquierda":
            salir = True
            cuarto_cinco()
        elif move == "derecha":
            salir = True
            cuarto_tres()
        elif move == objetos[6]:
            mochila[0], mochila[1], objetos[6] = objetos[6], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        elif move == objetos[7]:
            mochila[0], mochila[1], objetos[7] = objetos[7], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        else:
            print("no entiendo lo que quieres hacer")
            continue

def cuarto_cinco():

    print("\nEstás en la habitación número cinco. Aquí hay tres puertas")
    print("Tienes una puerta al frente, una a la izquierda y otra a la derecha. \nPuedes intentar abrir las")
    print(f"En la habitación hay dos objetos que tal vez te sirvan ({objetos[8]} y {objetos[9]}). ")
    print("Puedes guardarlos en tu mochila de a uno y solo puedes llevar dos objetos.")
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
        elif move == objetos[8]:
            mochila[0], mochila[1], objetos[8] = objetos[8], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        elif move == objetos[9]:
            mochila[0], mochila[1], objetos[9] = objetos[9], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        else:
            print("no entiendo lo que quieres hacer")
            continue

def cuarto_seis():

    print("\nEstás en la habitación número seis. Aquí hay una puerta")
    print("Tienes una puerta a la derecha. \nPuedes intentar la.")
    print(f"En la habitación hay dos objetos que tal vez te sirvan ({objetos[10]} y {objetos[11]}). ")
    print("Puedes guardarlos en tu mochila de a uno y solo puedes llevar dos objetos.")

    salir = False
    while not salir:
        move = input("Que vas a hacer? ")
        if move == "izquierda":
            salir = True
            print("Has abierto la puerta al infinito. Tu cuerpo flotará en el espacio por toda la eternidad.")
        elif move == "derecha":
            salir = True
            cuarto_cinco()
        elif move == objetos[10]:
            mochila[0], mochila[1], objetos[10] = objetos[10], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        elif move == objetos[11]:
            mochila[0], mochila[1], objetos[11] = objetos[11], mochila[0], mochila[1]
            print(f"En tu mochila hay {mochila[0]} y {mochila[1]}")
        else:
            print("no entiendo lo que quieres hacer")
            continue

cuarto_uno()
