
import random
from tqdm import tqdm
from time import sleep
import os
import winsound
import colorama
from colorama import Fore, init, Back, Style
init()
print(Fore.WHITE + Back.BLACK + Style.BRIGHT)
winsound.PlaySound("encendido.wav", winsound.SND_ASYNC)
print(Fore.GREEN + """

                                                        ██╗   ██╗    ███╗   ███╗    ██████╗ 
                                                        ██║   ██║    ████╗ ████║    ██╔══██╗
                                                        ██║   ██║    ██╔████╔██║    ██████╔╝
                                                        ██║   ██║    ██║╚██╔╝██║    ██╔══██╗
                                                        ╚██████╔╝    ██║ ╚═╝ ██║    ██████╔╝
                                                         ╚═════╝     ╚═╝     ╚═╝    ╚═════╝ 

""" + Fore.RESET )
tareas = 100
for i in tqdm(range(tareas)):
    sleep(0.01)
input("PRESIONA ENTER PARA CONTINUAR. ")
winsound.PlaySound("pat.wav", winsound.SND_LOOP)

print("""
                            BIENVENIDOS VIAJEROS, HAN LLEGADO HASTA MI JUEGO, ¿CÓMO? QUIEN SABE PERO YA ESTAM AQUI.
                            BIEN LES EXPLICO LAS REGLAS, SON SIMPLES:
                            CADA UNO TENDRA UN TURNO, EN EL CUAL PODRAS ELEGIR ENTRE ATACAR, RECUPERAR HP O RECUPERAR MP.
                            CONTARAS CON POCIONES DE HP O MP, LAS CUALES SERVIRAN PARA AUMENTAR EL HP Y MP RESPECTIVAMENTE.
                            ES SIMPLE ¿VERDAD? BUENO A VER QUIEN GANA.
                            SUERTE.
                            ANTES DE IRME, EN UN PRINCIPIO CONTARAS CON 100 DE HP, 100 DE MP Y 5 POCIONES DE HP Y 5 DE MP.
""")
class Personaje():
    def __init__(self):
        self.hp = 100
        self.mp = 100

    def aumentarHp(self):
        self.hp += 10

    def disminirHp(self):
        self.hp -= 10

    def aumentarMp(self):
        self.mp += 10

    def disminuirMp(self):
        self.mp -= 10

class Jugador(Personaje):
    def __init__(self):
        super().__init__()
        self.nombre = ""
        self.ataque = 1
        self.pociones_mp = 5
        self.pociones_hp = 5

    def recuperarHp(self):
        if self.pociones_hp >= 1:
            self.hp += 10
            self.pociones_hp -= 1

        else:
            print("Las pociones no son suficientes.")

    def recuperarMp(self):
        if self.pociones_mp >= 1:
            self.mp += 10
            self.pociones_mp -= 1
        else:
            print("Las posiciones no son suficientes.")



jugador_1 = Jugador()
jugador_1.nombre = input(Fore.CYAN + "\nBinvenido jugador 1 ingresa tu nombre:  " + Fore.RESET)
jugador_2 = Jugador()
jugador_2.nombre = input(Fore.MAGENTA + "\nBinvenido jugador 2 ingresa tu nombre:  " + Fore.RESET)
os.system("cls")
while jugador_1.hp > 0 and jugador_2.hp > 0:
    while jugador_1.hp > 0 and jugador_2.hp > 0:
        accion_jugador_1 = input( Fore.CYAN +f"""\n
                                                                    Hola {jugador_1.nombre}
                                                      _____________________________________________                
                                                     |          DIME, ¿QUÉ QUIERES HACER?          |      
                                                     |                                             |      
                                                     |  PRESIONA 1 PARA ATACAR                     |     
                                                     |                                             |            
                                                     |  PRESIONA 2 PARA RECUPERAR HP               |  
                                                     |                                             |              
                                                     |  PRESIONA 3 PARA RECUPERAR MP               |     
                                                     |_____________________________________________|   
"""+ Fore.RESET)
        if accion_jugador_1 == "1" and jugador_1.mp >= 10:
            danio = random.randrange(11)
            jugador_2.disminirHp()
            jugador_2.hp -= danio
            jugador_1.disminuirMp()

        elif accion_jugador_1 == "1" and jugador_1.mp == 0:
            danioo = 1
            jugador_2.hp -= danioo

        elif accion_jugador_1 == "1":
            jugador_2.disminirHp()
        elif accion_jugador_1 == "2":
            jugador_1.recuperarHp()

        elif accion_jugador_1 == "3":
            jugador_1.recuperarMp()

        else:
            print(Fore.CYAN + "ELIJE UNA OPCIÓN VALIDAAAAA. \n" + Fore.RESET)
        break
    sleep(0.3)
    print(Fore.CYAN + f"""
                                                      ╔══════════════════════════════════════════════╗
                                                       {jugador_1.nombre} Tus datos hasta ahora son:   
                                                       Pociones de Vida {jugador_1.pociones_hp * "*"}                
                                                       Pociones de Magia {jugador_1.pociones_mp * "*"}
                                                      ╚══════════════════════════════════════════════╝

    """ + Fore.RESET)
    while jugador_1.hp >= 1:
        a = "●" * jugador_1.hp
        print( Fore.CYAN + a , f"HP = {jugador_1.hp} ♡️" + Fore.RESET)
        break

    while jugador_1.mp >= 1:
        b = "●" * jugador_1.mp
        print(Fore.CYAN + b,  f"MP = {jugador_1.mp} ◕ \n" + Fore.RESET)
        break
    s = jugador_2.pociones_mp * "◕"
    sleep(0.3)
    print(Fore.MAGENTA + f"""
                                                      ╔══════════════════════════════════════════════╗
                                                       {jugador_2.nombre} Tus datos hasta ahora son: 
                                                       Pociones de Vida {jugador_2.pociones_hp * "*"}            
                                                       Pociones de Magia {jugador_2.pociones_mp * "*"}       
                                                      ╚══════════════════════════════════════════════╝
         """ + Fore.RESET)


    while jugador_2.hp >= 1:
        a = "●" * jugador_2.hp
        print(Fore.MAGENTA + a , f" HP = {jugador_2.hp} ♡" + Fore.RESET)
        break

    while jugador_2.mp >= 1:
        b = "●" * jugador_2.mp
        print(Fore.MAGENTA + b,  f"MP = {jugador_2.mp} ◕ \n"+ Fore.RESET)
        break
    input("Presiona enter para continuar.")
    os.system("cls")
    while jugador_1.hp > 0 and jugador_2.hp > 0:
        sleep(0.3)
        accion_jugador_2 = input(Fore.MAGENTA + f"""\n
                                                                    HOLA {jugador_2.nombre} 
                                                         _____________________________________________                
                                                        |          DIME ¿QUÉ QUIERES HACER?           |      
                                                        |                                             |      
                                                        |  PRESIONA 1 PARA ATACAR                     |     
                                                        |                                             |            
                                                        |  PRESIONA 2 PARA RECUPERAR HP               |  
                                                        |                                             |              
                                                        |  PRESIONA 3 PARA RECUPERAR MP               |     
                                                        |_____________________________________________|   

""" + Fore.RESET)
        if accion_jugador_2 == "1" and jugador_2.mp >= 10:
            jugador_1.disminirHp()
            danio = random.randrange(11)
            jugador_1.hp -= danio
            jugador_2.disminuirMp()

        elif accion_jugador_2 == "1" and jugador_1.mp == 0:
            danioo = 1
            jugador_1.hp -= danioo

        elif accion_jugador_2 == "1":
            jugador_1.disminirHp()

        elif accion_jugador_2 == "2":
            jugador_2.recuperarHp()

        elif accion_jugador_2 == "3":
            jugador_2.recuperarMp()

        else:
            print(Fore.MAGENTA + "ELIGE UNA OPCION VALIDAAAA. \n" + Fore.RESET)
        break

    sleep(0.3)
    print(Fore.MAGENTA + f"""
                                                      ╔══════════════════════════════════════════════╗
                                                       {jugador_2.nombre} Tus datos hasta ahora son: 
                                                       Pociones de Vida {jugador_2.pociones_hp * "*"}         
                                                       Pociones de Magia {jugador_2.pociones_mp * "*"}   
                                                      ╚══════════════════════════════════════════════╝
         """ + Fore.RESET)


    while jugador_2.hp >= 1:
        a = "●" * jugador_2.hp
        print(Fore.MAGENTA + a , f" HP = {jugador_2.hp} ♡" + Fore.RESET)
        break

    while jugador_2.mp >= 1:
        b = "●" * jugador_2.mp
        print(Fore.MAGENTA + b,  f"MP = {jugador_2.mp} ◕ \n"+ Fore.RESET)
        break
    sleep(0.3)
    print(Fore.CYAN + f"""
                                                         ╔══════════════════════════════════════════════╗
                                                          {jugador_1.nombre} Tus datos hasta ahora son:   
                                                          Pociones de Vida {jugador_1.pociones_hp * "*"}             
                                                          Pociones de Magia {jugador_1.pociones_mp * "*"}
                                                         ╚══════════════════════════════════════════════╝

       """ + Fore.RESET)
    while jugador_1.hp >= 1:
        a = "●" * jugador_1.hp
        print(Fore.CYAN + a, f"HP = {jugador_1.hp} ♡️" + Fore.RESET)
        break

    while jugador_1.mp >= 1:
        b = "●" * jugador_1.mp
        print(Fore.CYAN + b, f"MP = {jugador_1.mp} 🧙 \n" + Fore.RESET)
        break
    input("Presiona enter para continuar.")
    os.system("cls")
if jugador_1.hp <= 0 or jugador_2.hp <= 0:
    sleep(0.3)
    print("EL JUEGO HA TERMINADO. \n")
    winsound.PlaySound("apagado.wav", winsound.SND_ASYNC)

    if jugador_1.hp <= 0 and jugador_2.hp > 0:
        print(Fore.MAGENTA + f"EL GANADOR ES {jugador_2.nombre}" + Fore.RESET)
        print(Fore.YELLOW + """ TOMA TU PREMIO, MUCHAS FELICIDADES.
                                                                                     
                                                          **************                        .*************  .           
                                                      .   ,**        ***                        ,**        ***              
                                                           **       ,,,.......,,,,,,,,,,,,,*,,,,,,,,       **           .   
                                                           ***       ,,.......,,,,,,,,,,,,,,,,,,,**       ***          ..   
                                                         .  **       ,,,.......,,,,,,,,,,,,,,,,,,**       **                
                                                            .** .    ,,,.......,,,,,,,,,,,,,,,,,,**      ***                
                                                             ***      ,,.......,,,,,,,,,,,,,,,,,,*      ***                 
                                                              ***    .,,,......,,,,,,,,,,,,,,,,,**     ***                  
                                                               ***     ,,.......,,,,,,,,,,,,,,,,*.    ***                   
                                                                 **,   ,,,......,,,,,,,,,,,,,,,**    **                     
                                                                  ***   ,,,......,,,,,,,,,,,,,**   ***                      
                                                                    ***. ,,,.....,,,,,,,,,,,,,*  ***                        
                                                                      ,***,,,.....,,,,,,,,,,,*****                          
                                                                         ,**,,.....,,,,,,,,,***                             
                                                                              ,,....,,,,,,,                             .   
                                                           .                  .. *****/. ..                                 
                                                         .                       ,,.,,*.                                    
                                                                                 .,.,,*       .                             
                                                                                 ,,.,,*                                     
                                                                                 ,,.,,,            .                        
                                                                                ,,.,,,,*                                    
                                                                               /,..,,,,,*                                   
                                              .                             ###(/((((((((((#                                
                                                                            ##((/(((((((((((*                .              
                                                                           ###((((((((((((((#                               
                                                                           ##(((((((((((((((#.                    .         
                                                                          ###((#(((((((((((((#                          .   
                                                           .                             ..      
               """ + Fore.RESET)
        print(Fore.CYAN + f"TU PIERDES {jugador_1.nombre}" + Fore.RESET)
        print(Fore.YELLOW + """ TEN TU.
             (((...........)))          
           (((..............)))         
          (((................)))         
          (((.................)))         
          (((.................)))         
           (((...............)))          
             /..............\            
            /....../\.......\           
           /....../   \.......\          
          /....../     \.......\         
         /....../       \.......\        
        /....../         \.......\          
                                                       
               """ + Fore.RESET)

    elif jugador_2.hp <= 0 and jugador_1.hp > 0:
        print(Fore.CYAN + f"EL GANADOR ES {jugador_1.nombre}" + Fore.RESET)
        print(Fore.YELLOW + """ MUCHAS FELICIDADES TOMA.             
                                                           **       ,,,.......,,,,,,,,,,,,,*,,,,,,,,       **           .   
                                                           ***       ,,.......,,,,,,,,,,,,,,,,,,,**       ***          ..   
                                                         .  **       ,,,.......,,,,,,,,,,,,,,,,,,**       **                
                                                            .** .    ,,,.......,,,,,,,,,,,,,,,,,,**      ***                
                                                             ***      ,,.......,,,,,,,,,,,,,,,,,,*      ***                 
                                                              ***    .,,,......,,,,,,,,,,,,,,,,,**     ***                  
                                                               ***     ,,.......,,,,,,,,,,,,,,,,*.    ***                   
                                                                 **,   ,,,......,,,,,,,,,,,,,,,**    **                     
                                                                  ***   ,,,......,,,,,,,,,,,,,**   ***                      
                                                                    ***. ,,,.....,,,,,,,,,,,,,*  ***                        
                                                                      ,***,,,.....,,,,,,,,,,,*****                          
                                                                         ,**,,.....,,,,,,,,,***                             
                                                                              ,,....,,,,,,,                             .   
                                                           .                  .. *****/. ..                                 
                                                         .                       ,,.,,*.                                    
                                                                                 .,.,,*       .                             
                                                                                 ,,.,,*                                     
                                                                                 ,,.,,,            .                        
                                                                                ,,.,,,,*                                    
                                                                               /,..,,,,,*                                   
                                              .                             ###(/((((((((((#                                
                                                                            ##((/(((((((((((*                .              
                                                                           ###((((((((((((((#                               
                                                                           ##(((((((((((((((#.                    .                                  .   
                                                           .                             ..      
               """ + Fore.RESET)
        print(Fore.MAGENTA + f"TU PIERDES {jugador_2.nombre}" + Fore.RESET)
        print(Fore.YELLOW+ """ TEN TU.     
                                                                  
             (((...........)))          
           (((..............)))         
          (((................)))         
          (((.................)))         
          (((.................)))         
           (((...............)))          
             /..............\            
            /....../\.......\           
           /....../   \.......\          
          /....../     \.......\         
         /....../       \.......\        
        /....../         \.......\                   
        """+ Fore.RESET)
input("presiona enter para continuar")
os.system("cls")
os.system("python main.py")


