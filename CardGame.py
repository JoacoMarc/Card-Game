import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import os
from colorama import init

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

# Ruta donde se encuentran las imágenes de las cartas
cartas_dir = "cartas"

# Función para obtener la ruta de la imagen de la carta
def obtener_ruta_carta(carta):
    numero, palo = carta.split(' de ')
    nombre_archivo = f"{palo.lower()}{numero}.jpg"
    return os.path.join(cartas_dir, nombre_archivo)

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

def valor_carta_truco(carta):
    return jerarquia.get(carta, 0)

class TrucoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Cartas Truco")
        self.cartas = []
        self.rondas_ganadas = []
        self.jugadores = 0
        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="Bienvenido al Juego de Cartas Truco", font=('Arial', 24, 'bold'))
        self.label.pack(pady=20)

        self.jugadores_label = tk.Label(self.root, text="Cantidad de jugadores (2 a 6):", font=('Arial', 16))
        self.jugadores_label.pack()

        self.jugadores_entry = tk.Entry(self.root, font=('Arial', 14))
        self.jugadores_entry.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Iniciar Juego", command=self.iniciar_juego, font=('Arial', 14))
        self.start_button.pack(pady=20)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=('Arial', 14))
        self.exit_button.pack(pady=10)

    def iniciar_juego(self):
        try:
            self.jugadores = int(self.jugadores_entry.get())
            if self.jugadores < 2 or self.jugadores > 6:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido de jugadores (2 a 6).")
            return

        self.cartas = distribuircartas(self.jugadores)
        self.rondas_ganadas = [0] * self.jugadores
        self.ronda = 1

        self.jugar_ronda()

    def jugar_ronda(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.ronda_label = tk.Label(self.root, text=f"Ronda {self.ronda}", font=('Arial', 20, 'bold'))
        self.ronda_label.pack(pady=20)

        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.cartas_tiradas = []
        self.jugador_actual = 0
        self.mostrar_elegir_carta()

    def mostrar_elegir_carta(self):
        if self.jugador_actual >= self.jugadores:
            self.determinar_ganador_ronda()
            return

        jugador = self.cartas[self.jugador_actual]
        self.elegir_carta_label = tk.Label(self.scrollable_frame, text=f"Jugador {self.jugador_actual + 1}, elige una carta:", font=('Arial', 16, 'bold'))
        self.elegir_carta_label.pack(pady=10)

        self.cartas_frame = tk.Frame(self.scrollable_frame)
        self.cartas_frame.pack()

        for carta in jugador:
            image_path = obtener_ruta_carta(carta)
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = image.resize((100, 150), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                carta_button = tk.Button(self.cartas_frame, image=photo, command=lambda c=carta: self.tirar_carta(c))
                carta_button.image = photo
                carta_button.pack(side=tk.LEFT, padx=5)
            else:
                print(f"Error: No se encontró la imagen para la carta {carta}")

    def tirar_carta(self, carta):
        self.cartas_tiradas.append((self.jugador_actual + 1, carta))
        self.cartas[self.jugador_actual].remove(carta)
        self.jugador_actual += 1
        if self.jugador_actual < self.jugadores:
            self.mostrar_elegir_carta()
        else:
            self.determinar_ganador_ronda()

    def determinar_ganador_ronda(self):
        mejor_valor = 0
        ganadores = []
        mejor_carta = ""
        for jugador, carta in self.cartas_tiradas:
            valor = valor_carta_truco(carta)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_carta = carta
                ganadores = [jugador]
            elif valor == mejor_valor:
                ganadores.append(jugador)
        
        if len(ganadores) > 1:
            self.mensaje_empate(ganadores)
        else:
            ganador = ganadores[0]
            self.rondas_ganadas[ganador - 1] += 1
            self.mostrar_ganador_ronda(ganador, mejor_carta)

        if max(self.rondas_ganadas) == 2:
            self.determinar_ganador_juego()
        elif self.ronda == 3:
            self.determinar_ganador_juego()
        else:
            self.ronda += 1
            self.jugar_ronda()

    def mensaje_empate(self, ganadores):
        empates_texto = ', '.join([f"Jugador {g}" for g in ganadores])
        messagebox.showinfo("Empate", f"Empate entre {empates_texto}.")
        self.cartas_tiradas = []
        self.jugador_actual = 0
        self.mostrar_elegir_carta()

    def mostrar_ganador_ronda(self, ganador, carta):
        messagebox.showinfo("Ganador de la Ronda", f"El ganador de la ronda {self.ronda} es el Jugador {ganador} con la carta {carta}.")
        self.cartas_tiradas = []
        self.jugador_actual = 0

    def determinar_ganador_juego(self):
        max_rondas_ganadas = max(self.rondas_ganadas)
        ganadores_finales = [i + 1 for i, x in enumerate(self.rondas_ganadas) if x == max_rondas_ganadas]

        if len(ganadores_finales) > 1:
            ganadores_texto = ', '.join([f"Jugador {g}" for g in ganadores_finales])
            messagebox.showinfo("Empate", f"¡Hay un empate entre {ganadores_texto} con {max_rondas_ganadas} rondas ganadas!")
        else:
            ganador_final = ganadores_finales[0]
            messagebox.showinfo("Ganador del Juego", f"¡El ganador final es el Jugador {ganador_final} con {max_rondas_ganadas} rondas ganadas!")

        self.volver_al_menu()

    def volver_al_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.setup_ui()

def main():
    root = tk.Tk()
    app = TrucoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
