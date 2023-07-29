import tkinter as tk
from tkinter import messagebox

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def add_element(self, key, value):
        index = self._hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def get_element(self, key):
        index = self._hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

def add_element_to_hash_table():
    key = key_entry.get()
    value = value_entry.get()

    if key and value:
        hash_table.add_element(key, value)
        messagebox.showinfo("Éxito", f"Elemento agregado: {key} -> {value}")
    else:
        messagebox.showerror("Error", "Por favor, ingresa un valor clave y un valor asociado.")

def search_element_in_hash_table():
    key = key_entry.get()

    if key:
        value = hash_table.get_element(key)
        if value:
            messagebox.showinfo("Resultado", f"Valor asociado para '{key}': {value}")
        else:
            messagebox.showinfo("Resultado", f"El elemento '{key}' no se encontró en la tabla.")
    else:
        messagebox.showerror("Error", "Por favor, ingresa un valor clave.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Tabla Hash")

hash_table = HashTable()

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

key_label = tk.Label(frame, text="Clave:")
key_label.grid(row=0, column=0, padx=5, pady=5)

key_entry = tk.Entry(frame)
key_entry.grid(row=0, column=1, padx=5, pady=5)

value_label = tk.Label(frame, text="Valor:")
value_label.grid(row=1, column=0, padx=5, pady=5)

value_entry = tk.Entry(frame)
value_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Agregar", command=add_element_to_hash_table)
add_button.grid(row=2, column=0, padx=5, pady=5)

search_button = tk.Button(frame, text="Buscar", command=search_element_in_hash_table)
search_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
