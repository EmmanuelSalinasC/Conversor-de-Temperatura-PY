import tkinter as tk
from tkinter import messagebox

def convert_to_fahrenheit():
    try:
        celsius = float(tbCelsius.get())
        fahrenheit = (celsius * 9 / 5) + 32
        tbFahrenheit.delete(0, tk.END)
        tbFahrenheit.insert(0, str(round(fahrenheit, 2)))
    except ValueError:
        messagebox.showerror("Error", "inserte numero valido para Celsius.")

def convert_to_celsius():
    try:
        fahrenheit = float(tbFahrenheit.get())
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        tbCelsius.delete(0, tk.END)
        tbCelsius.insert(0, str(round(celsius, 2)))
    except ValueError:
        messagebox.showerror("Error", "Inserte numero valido para Fahrenheit.")

def clear_fields():
    tbCelsius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("400x200")

lbFahrenheit = tk.Label(ventana, text="Fahrenheit:")
lbFahrenheit.grid(row=0, column=0, padx=10, pady=10)
tbFahrenheit = tk.Entry(ventana)
tbFahrenheit.grid(row=0, column=1, padx=10, pady=10)
btnFahrenheit = tk.Button(ventana, text="Convertir a Celsius", command=convert_to_celsius)
btnFahrenheit.grid(row=0, column=2, padx=10, pady=10)

lbCelsius = tk.Label(ventana, text="Celsius:")
lbCelsius.grid(row=1, column=0, padx=10, pady=10)
tbCelsius = tk.Entry(ventana)
tbCelsius.grid(row=1, column=1, padx=10, pady=10)
btnCelsius = tk.Button(ventana, text="Convertir a Fahrenheit", command=convert_to_fahrenheit)
btnCelsius.grid(row=1, column=2, padx=10, pady=10)

btnClear = tk.Button(ventana, text="Limpiar", command=clear_fields)
btnClear.grid(row=2, column=0, columnspan=3, pady=10)

ventana.mainloop()