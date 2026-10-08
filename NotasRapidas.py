import tkinter as tk
from tkinter import simpledialog, messagebox

# Clase principal de la aplicación
class NotasApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # Configuración del titulo y tamaño que tendra la ventana
        self.title("Notas Rápidas (Tkinter)")
        self.geometry("600x380")

        # Variable que ayuda a llevar y mostrar la cantidad de notas que tiene el programa.
        self.var_contador = tk.StringVar(value="0 notas")

        #Este es el espacio creado donde el usuario pueda escribir una nota.
        self.input = tk.Entry(self)
        self.input.pack(fill="x", padx=8, pady=8)

        # Permite agregar una nota al presionar la tecla Enter
        self.input.bind("<Return>", lambda e: self.agregar())

        # Marco que contiene los botones y el contador
        frame_btns = tk.Frame(self)
        frame_btns.pack(fill="x", padx=8)

        # Botón que se utiliza para agregar una nota 
        tk.Button(
            frame_btns,
            text="Agregar",
            command=self.agregar
        ).pack(side="left")

        # Botón que sirve para eliminar una nota seleccionada
        tk.Button(
            frame_btns,
            text="Eliminar",
            command=self.eliminar
        ).pack(side="left", padx=6)

        # Etiqueta que muestra la cantidad de notas que llevamos
        tk.Label(
            frame_btns,
            textvariable=self.var_contador
        ).pack(side="left", padx=12)

        # Lista donde se muestran las notas
        self.lista = tk.Listbox(self)
        self.lista.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        # Permite editar una nota al hacer doble click
        self.lista.bind(
            "<Double-Button-1>",
            self.editar_item
        )

        # Lista donde se almacenan las notas
        self.notas = []

        # Actualiza el contador al iniciar el programa
        self.actualizar_contador()

    # Actualiza la cantidad de notas mostrada en la ventana
    def actualizar_contador(self):
        n = len(self.notas)

        if n == 1:
            self.var_contador.set("1 nota")
        else:
            self.var_contador.set(f"{n} notas")

    # Agrega una nueva nota a la lista
    def agregar(self):
        texto = self.input.get().strip()

        # Verifica que el usuario haya escrito algo
        if texto:
            self.notas.append(texto)

            # Muestra la nota en el Listbox
            self.lista.insert("end", texto)

            # Limpia el campo de texto
            self.input.delete(0, "end")

            # Actualiza el contador
            self.actualizar_contador()

    # permite eliminar la nota seleccionada
    def eliminar(self):
        sel = self.lista.curselection()

        # Si no hay ninguna nota seleccionada, muestra un mensaje
        if not sel:
            messagebox.showinfo(
                "Eliminar",
                "Selecciona una nota."
            )
            return

        # permite obtener la posición de la nota seleccionada
        idx = sel[0]

        # permite eliminar la nota de la lista
        self.lista.delete(idx)

        # perimite eliminar la nota de la lista interna
        self.notas.pop(idx)

        # Encargado de actualizar el contador
        self.actualizar_contador()

    # permite editar una nota cuando el usuario hace doble clic
    def editar_item(self, event=None):
        sel = self.lista.curselection()

        # Verifica que exista una nota seleccionada
        if not sel:
            return

        # Obtiene la posición de la nota seleccionada
        idx = sel[0]

        # Obtiene el texto actual de la nota
        actual = self.notas[idx]

        # Abre una ventana para solicitar el nuevo texto a ingresar
        nuevo = simpledialog.askstring(
            "Editar nota",
            "Nuevo texto:",
            initialvalue=actual
        )

        # Actualiza la nota si el usuario escribió un nuevo texto
        if nuevo and nuevo.strip():
            nuevo = nuevo.strip()

            self.notas[idx] = nuevo

            # Actualiza la nota mostrada en el Listbox
            self.lista.delete(idx)
            self.lista.insert(idx, nuevo)


# Encaragado de iniciar la app
if __name__ == "__main__":
    NotasApp().mainloop()