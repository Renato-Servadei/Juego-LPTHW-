mochila = ["", ""]
objetos = {"cuarto_uno": ["Destornillador", "Mancuerna"], 
           "cuarto_dos": ["Pelota", "Llave"],
           "cuarto_tres":["Termo", "Celular"],
           "cuarto_cuatro":["Manzana", "Billetera"],
           "cuarto_cinco": ["Mate", "Bicicleta"],
           "cuarto_seis":["Campera", "Radio"]
            }
cuartos = list(objetos.keys())
cuarto_actual = cuartos[0]
puertas = {
            "cuarto_uno": {"izquierda": "salida", "derecha":cuartos[1]},
            "cuarto_dos": {"izquierda": cuartos[0], "derecha": cuartos[2], "frente": cuartos[4] },
            "cuarto_tres": {"izquierda": cuartos[1], "derecha": cuartos[3]},
            "cuarto_cuatro": {"izquierda": cuartos[4], "derecha": cuartos[2]},
            "cuarto_cinco": {"izquierda": "cuarto_seis", "derecha": cuartos[3], "frente": cuartos[1] },
            "cuarto_seis": {"derecha": cuartos[4]}
            }

def jugar():
    print(f"\nEstás en la habitación número {(cuartos.index(cuarto_actual)+1)}. Hay "\
          f"{len(puertas[cuarto_actual])} puertas. {list(puertas[cuarto_actual].keys())}" \
            "\nPuedes intentar abrirlas")
    print(f"En la habitación hay dos objetos que tal vez te sirvan ({objetos[cuarto_actual][0]} y {objetos[cuarto_actual][1]}). ")
    print("Puedes guardarlos en tu mochila de a uno y solo puedes llevar dos objetos.")
    
    while True:
        move = input("Que quieres hacer? ").strip().lower()
        if move in puertas[cuarto_actual]:
            cambiar_cuartos(move)

        if move in objetos[cuarto_actual]:
            indice = objetos[cuarto_actual].index(move)
            guardar(indice)

        else: 
            print("No entendí lo que quieres hacer")

def cambiar_cuartos(move):
    
    global cuarto_actual
    if puertas[cuarto_actual][move] == "salida":
        salir()
    else: 
        cuarto_actual = puertas[cuarto_actual][move]
        jugar()

def salir():
    if 'Termo' in mochila and 'Mate' in mochila:
        print('Lo has logrado, nunca salgas de sin tu mate y tu termo')
        exit()
    else:
        print('No tienes los objetos necesarios para salir. Sigue buscando.')
        jugar()

def guardar(indice):
    mochila[0], mochila[1], objetos[cuarto_actual][indice] = objetos[cuarto_actual][indice], mochila[0], mochila[1]
    print(f'Ahora en tu mochila tienes: {mochila}')
    print(f'En el cuarto queda: {objetos[cuarto_actual]}')


jugar()
