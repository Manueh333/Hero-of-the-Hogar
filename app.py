import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def arte_exterior():
    print("""
       ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
  |                      |
    === LA PUERTA ESTÁ CERRADA ===
    """)

def arte_salon():
    print("""
      ________________________
     |  __   __   __         |
     | |  | |  | |  |  [TV]  |
     | |__| |__| |__|        |
     |                       |
     |       [ SOFÁ ]        |
     |_______________________|
     --- ESTÁS EN EL SALÓN ---
    """)

def arte_futbol():
    print("""
       ___________
      |  |     |  |
      |  |  O  |  |  <-- ¡GOOOOOL!
      |__|_____|__|
         \\___/
    """)

def arte_barrer():
    print("""
         //
        //
       //
      //
     /__\\
    ||||||  <-- Barriendo las pelusas...
    """)

def arte_cocina():
    print("""
      ________________________
     | [NEVERA]   [FREGADERO]|
     |                       |
     |        [MESA]         |
     |                       |
     |_______________________|
     --- ESTÁS EN LA COCINA ---
    """)

def arte_fregando():
    print("""
        \\  /
      __\\/__
     |      |
     | (o)  |  <-- Platos relucientes
     |______|
    """)

def arte_lavadero():
    print("""
      ________________________
     |                       |
     |     [LAVADORA]        |
     |     [CESTO ROPA]      |
     |                       |
     |_______________________|
    --- ESTÁS EN EL LAVADERO ---
    """)

def arte_lavadora_funcionando():
    print("""
       __________
      |  ______  |
      | /  _   \\ |
      | | (_)  | | <-- brum brum... centrifugando...
      | \\______/ |
      |__________|
    """)

def arte_manulleta():
    print("""
         ____
       / o   \\
      |  o  o |  <-- ¡LA MANULLETA LEGENDARIA!
       \\___o_/
    """)

def main():
    habitacion = "exterior"
    energia = 60
    miradas_izquierda = 0
    
    tareas = {
        "lavadora": {"nombre": "Poner la lavadora (Lavadero)", "hecha": False, "coste": 15},
        "barrer": {"nombre": "Barrer el suelo (Salón)", "hecha": False, "coste": 20},
        "platos": {"nombre": "Fregar los platos (Cocina)", "hecha": False, "coste": 15}
    }

    while True:
        limpiar_pantalla()
        print("=== BOCKATHOM 2026: HERO OF THE HOGAR ===")
        print(f"Energía: {'#' * (energia // 10)} ({energia}%)")
        print("-----------------------------------------\n")

        todas_hechas = all(t["hecha"] for t in tareas.values())
        if todas_hechas:
            print("¡VICTORIA NORMAL! Has terminado todas las tareas de la casa.")
            break
        if energia <= 0:
            print("¡GAME OVER! Te quedaste sin energía en medio de la limpieza.")
            break

        if habitacion == "exterior":
            arte_exterior()
            print("1. Entrar a la casa")
            print("2. Rendirse y huir")
            opcion = input("\nElige: ")
            if opcion == "1":
                habitacion = "salon"
            elif opcion == "2":
                break
                
        elif habitacion == "salon":
            arte_salon()
            print("1. Ir a la Cocina")
            print("2. Ir al Lavadero")
            print("3. Barrer el suelo (-20 energía)")
            print("4. Sentarse en el sofá a ver el fútbol (+40 energía)")
            opcion = input("\nElige: ")
            
            if opcion == "1": habitacion = "cocina"
            elif opcion == "2": habitacion = "lavadero"
            elif opcion == "3":
                if not tareas["barrer"]["hecha"]:
                    if energia >= 20:
                        limpiar_pantalla()
                        arte_barrer()
                        print("\nBarriendo el salón... quitando las pelusas...")
                        time.sleep(2)
                        tareas["barrer"]["hecha"] = True
                        energia -= 20
                    else:
                        print("\nNo tienes energía.")
                        time.sleep(1)
                else:
                    print("\nYa está barrido.")
                    time.sleep(1)
            elif opcion == "4":
                limpiar_pantalla()
                arte_futbol()
                print("\nDisfrutando del partido... ¡Qué golazo!")
                time.sleep(3)
                energia = min(100, energia + 40)
                
        elif habitacion == "cocina":
            arte_cocina()
            print("1. Volver al Salón")
            if not tareas["platos"]["hecha"]:
                print("2. Fregar los platos (-15 energía)")
            else:
                print("2. Fregar los platos (Ya está hecho, pero puedes seguir en el fregadero)")
                
            opcion = input("\nElige: ")
            if opcion == "1": 
                habitacion = "salon"
                miradas_izquierda = 0
            elif opcion == "2":
                if not tareas["platos"]["hecha"] and energia >= 15:
                    limpiar_pantalla()
                    arte_fregando()
                    print("\nFregando los platos... quitando la grasa incrustada...")
                    tareas["platos"]["hecha"] = True
                    energia -= 15
                    time.sleep(2)
                
                while True:
                    limpiar_pantalla()
                    arte_cocina()
                    print("\nEstás frente al fregadero con las manos mojadas.")
                    print("1. Dejar de fregar")
                    print("2. Mirar a la izquierda")
                    sub_op = input("\nElige: ")
                    
                    if sub_op == "1":
                        break
                    elif sub_op == "2":
                        miradas_izquierda += 1
                        if miradas_izquierda == 1:
                            print("\nMiras a la izquierda... No hay nada, solo la pared y un azulejo roto.")
                            time.sleep(2)
                        elif miradas_izquierda == 2:
                            limpiar_pantalla()
                            arte_manulleta()
                            print("\n¡HAS ENCONTRADO LA MANULLETA OCULTA TRAS EL ESCURREPLATOS!")
                            print("Te la comes, el azúcar te da poderes cósmicos.")
                            print("¡La casa se limpia sola! ¡VICTORIA ABSOLUTA Y SECRETA!")
                            time.sleep(5)
                            return 
                        
        elif habitacion == "lavadero":
            arte_lavadero()
            print("1. Volver al Salón")
            print("2. Poner la lavadora (-15 energía)")
            opcion = input("\nElige: ")
            if opcion == "1": habitacion = "salon"
            elif opcion == "2":
                if not tareas["lavadora"]["hecha"] and energia >= 15:
                    limpiar_pantalla()
                    arte_lavadora_funcionando()
                    print("\nBrum brum... lavadora puesta en ciclo de algodón.")
                    tareas["lavadora"]["hecha"] = True
                    energia -= 15
                    time.sleep(2)
                elif tareas["lavadora"]["hecha"]:
                    print("\nLa lavadora ya está funcionando.")
                    time.sleep(1)
                else:
                    print("\nEstás muy cansado para levantar la ropa. Toca ver el fútbol.")
                    time.sleep(2)

if __name__ == "__main__":
    main()
