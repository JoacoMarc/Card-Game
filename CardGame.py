import random
from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

# Definición de las jerarquías en el truco
jerarquia = {
    "1 de Espadas": 14, "1 de Bastos": 13, "7 de Espadas": 12, "7 de Oros": 11,
    "3 de Oros": 10, "3 de Copas": 10, "3 de Espadas": 10, "3 de Bastos": 10,
    "2 de Oros": 9, "2 de Copas": 9, "2 de Espadas": 9, "2 de Bastos": 9,
    "1 de Copas": 8, "1 de Oros": 8,
    "12 de Oros": 7, "12 de Copas": 7, "12 de Espadas": 7, "12 de Bastos": 7,
    "11 de Oros": 6, "11 de Copas": 6, "11 de Espadas": 6, "11 de Bastos": 6,
    "10 de Oros": 5, "10 de Copas": 5, "10 de Espadas": 5, "10 de Bastos": 5,
    "7 de Copas": 4, "7 de Bastos": 4,
    "6 de Oros": 3, "6 de Copas": 3, "6 de Espadas": 3, "6 de Bastos": 3,
    "5 de Oros": 2, "5 de Copas": 2, "5 de Espadas": 2, "5 de Bastos": 2,
    "4 de Oros": 1, "4 de Copas": 1, "4 de Espadas": 1, "4 de Bastos": 1
}

def distribuircartas(jugadores):
    listacartas = [f"{n} de {palo}" for palo in ["Oros", "Copas", "Bastos", "Espadas"] for n in range(1, 13) if n not in [8, 9]]
    mano = []
    for _ in range(jugadores * 3):  # Tres cartas por jugador
        carta = random.choice(listacartas)
        mano.append(carta)
        listacartas.remove(carta)
    matriz = []
    for i in range(jugadores):
        matriz.append(mano[i * 3:i * 3 + 3])
    return matriz

def mostrar_cartas(cartas):
    for i, jugador in enumerate(cartas):
        print(Fore.WHITE + f"Jugador {i+1}:  ", end="")
        for carta in jugador:
            print(f"{Fore.YELLOW}{carta:15}", end="")
        print(Style.RESET_ALL)

def valor_carta_truco(carta):
    return jerarquia.get(carta, 0)

def elegir_carta(jugador):
    print(Fore.WHITE + f"Tus cartas son: " + Fore.YELLOW + f"{', '.join(jugador)}")
    print()
    while True:
        eleccion = input("Elige una carta para tirar: " + Style.RESET_ALL)
        if eleccion in jugador:
            jugador.remove(eleccion)
            return eleccion
        else:
            print(Fore.RED + "Carta no válida, por favor elige una carta de tu mano.")

def jugar_ronda(cartas):
    cartas_tiradas = []
    for i, jugador in enumerate(cartas):
        print(f"\n{Fore.LIGHTBLACK_EX}Jugador {i + 1}")
        carta = elegir_carta(jugador)
        cartas_tiradas.append((i + 1, carta))
        print(Fore.LIGHTBLACK_EX + f"\n< Jugador {i + 1} tira {carta} >")

    mejor_valor = 0
    ganadores = []
    mejor_carta = ""
    for jugador, carta in cartas_tiradas:
        valor = valor_carta_truco(carta)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_carta = carta
            ganadores = [jugador]
        elif valor == mejor_valor:
            ganadores.append(jugador)
    
    if len(ganadores) > 1:
        print(Fore.LIGHTMAGENTA_EX + f"\nEmpate entre Jugadores: " + Fore.WHITE + f"{' y '.join(map(str, ganadores))}")
        return jugar_desempate(cartas, ganadores)
    else:
        return ganadores[0], mejor_carta

def jugar_desempate(cartas, ganadores):
    print(Fore.LIGHTGREEN_EX + "Desempate!")
    cartas_desempate = [cartas[jugador - 1] for jugador in ganadores]
    return jugar_ronda(cartas_desempate)

# Programa principal
print(Fore.MAGENTA + Style.BRIGHT + "=============================")
print(Fore.CYAN + Style.BRIGHT + "Bienvenido al Juego de Cartas")
print(Fore.MAGENTA + Style.BRIGHT + "=============================", end="\n\n")
jug = int(input("\nCantidad de jugadores " + Fore.MAGENTA + f"(2 a 6)" + Fore.WHITE + f":"))
while jug < 2 or jug > 6:
    jug = int(input("Cantidad de jugadores " + Fore.MAGENTA + f"(2 a 6)" + Fore.WHITE + f":"))

print()
cartas = distribuircartas(jug)
mostrar_cartas(cartas)

rondas_ganadas = [0] * jug
ronda = 1
while ronda <= 3:
    print(Fore.WHITE + Style.BRIGHT + "\n========")
    print(f"{Fore.LIGHTGREEN_EX}Ronda {ronda}")
    print(Fore.WHITE + Style.BRIGHT + "========")
    ganador, mejor_carta = jugar_ronda(cartas)
    rondas_ganadas[ganador - 1] += 1
    print()
    print(Fore.LIGHTMAGENTA_EX + f"El ganador de la ronda {ronda} es el: " + Fore.WHITE + f"Jugador {ganador}")
    
    if ronda == 2 and rondas_ganadas.count(max(rondas_ganadas)) > 1:
        ronda += 1
    elif ronda == 3:
        break
    ronda += 1

# Verificar si hay empate en rondas ganadas
max_rondas_ganadas = max(rondas_ganadas)
ganadores_finales = [i + 1 for i, x in enumerate(rondas_ganadas) if x == max_rondas_ganadas]

if len(ganadores_finales) > 1:
    print(f"\n{Fore.YELLOW}¡Hay un empate entre los Jugadores {', '.join(map(str, ganadores_finales))} con {max_rondas_ganadas} rondas ganadas!")
else:
    ganador_final = ganadores_finales[0]
    print(f"\n{Fore.YELLOW}¡El ganador final es el Jugador {ganador_final} con {max_rondas_ganadas} rondas ganadas!")
