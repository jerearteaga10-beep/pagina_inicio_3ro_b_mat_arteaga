import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Para mostrar alertas de error o confirmación

# 1. Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("crud de productos -panel de control")
ventana.geometry("550x650")
ventana.resizable(False, False)


# --- FUNCIONES PARA MANEJAR LOS DATOS ---

def agregar_producto():
    # Obtener los datos de los campos de texto
    codigo = entry_codigo.get()
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    stock = entry_stock.get()
    
    # Validación simple: que no haya campos vacíos
    if codigo == "" or nombre == "" or precio == "" or stock == "":
        messagebox.showwarning("Campos vacíos", "Por favor, llena todos los campos.")
        return
    
    # Insertar en la tabla (Treeview)
    tabla.insert("", "end", values=(codigo, nombre, f"${precio}", stock))
    
    # Limpiar los campos después de agregar
    limpiar_campos()

def eliminar_producto():
    # Obtener el elemento seleccionado de la tabla
    seleccion = tabla.selection()
    
    if not seleccion:
        messagebox.showwarning("Sin selección", "Por favor, selecciona un producto de la tabla.")
        return
    
    # Confirmar eliminación
    resp = messagebox.askyesno("Eliminar", "¿Estás seguro de eliminar este producto?")
    if resp:
        for elemento in seleccion:
            tabla.delete(elemento)
        limpiar_campos()

def actualizar_producto():
    seleccion = tabla.selection()
    
    if not seleccion:
        messagebox.showwarning("Sin selección", "Selecciona el producto que deseas actualizar.")
        return
    
    codigo = entry_codigo.get()
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    stock = entry_stock.get()
    
    if codigo == "" or nombre == "" or precio == "" or stock == "":
        messagebox.showwarning("Campos vacíos", "Los campos no pueden quedar vacíos al actualizar.")
        return
    
    # Reemplazar los valores del elemento seleccionado
    # Si el precio ya trae el '$', evitamos duplicarlo
    precio_formateado = precio if "$" in precio else f"${precio}"
    tabla.item(seleccion[0], values=(codigo, nombre, precio_formateado, stock))
    limpiar_campos()

def al_seleccionar_fila(event):
    """Función para que al dar clic en la tabla, los datos suban al formulario"""
    seleccion = tabla.selection()
    if seleccion:
        # Obtener los valores de la fila seleccionada
        valores = tabla.item(seleccion[0], "values")
        
        # Limpiar entradas primero
        limpiar_campos()
        
        # Insertar los valores en los Entrys
        entry_codigo.insert(0, valores[0])
        entry_nombre.insert(0, valores[1])
        # Le quitamos el '$' al precio para poder editar el número limpio
        entry_precio.insert(0, valores[2].replace("$", ""))
        entry_stock.insert(0, valores[3])

def limpiar_campos():
    """Borra el texto de todas las cajas de entrada"""
    entry_codigo.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_stock.delete(0, tk.END)


# 2. frame para elformulario (entrada de datos)
frame_formulario = tk.LabelFrame(ventana, text=" datos de producto ", padx=10, pady=10)
frame_formulario.pack(fill="x", padx=15, pady=15)

# Campos del formulario
tk.Label(frame_formulario, text="Código:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_codigo = tk.Entry(frame_formulario)
entry_codigo.grid(row=0, column=1, fill="x", expand=True, padx=5, pady=5)

tk.Label(frame_formulario, text="Nombre:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_nombre = tk.Entry(frame_formulario)
entry_nombre.grid(row=1, column=1, fill="x", expand=True, padx=5, pady=5)

tk.Label(frame_formulario, text="Precio ($):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_precio = tk.Entry(frame_formulario)
entry_precio.grid(row=2, column=1, fill="x", expand=True, padx=5, pady=5)

tk.Label(frame_formulario, text="Stock:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
entry_stock = tk.Entry(frame_formulario)
entry_stock.grid(row=3, column=1, fill="x", expand=True, padx=5, pady=5)

# Botones de acción (Conectados a las funciones mediante 'command')
frame_botones = tk.Frame(frame_formulario)
frame_botones.grid(row=4, column=0, columnspan=2, pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar", width=10, command=agregar_producto)
btn_agregar.pack(side="left", padx=5)

btn_actualizar = tk.Button(frame_botones, text="Actualizar", width=10, command=actualizar_producto)
btn_actualizar.pack(side="left", padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=10, command=eliminar_producto)
btn_eliminar.pack(side="left", padx=5)


# 3. frame para la trabla (visualización de datos)
frame_tabla = tk.LabelFrame(ventana, text=" productos registros ", padx=10, pady=10)
frame_tabla.pack(fill="both", expand=True, padx=15, pady=15)

# Configuración de la Tabla (Treeview)
columnas = ("codigo", "nombre", "precio", "stock")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

tabla.heading("codigo", text="Código")
tabla.heading("nombre", text="Nombre del Producto")
tabla.heading("precio", text="Precio")
tabla.heading("stock", text="Stock")

tabla.column("codigo", width=80, anchor="center")
tabla.column("nombre", width=180, anchor="w")
tabla.column("precio", width=80, anchor="center")
tabla.column("stock", width=80, anchor="center")

scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Evento: Cuando el usuario hace clic en una fila de la tabla, llama a 'al_seleccionar_fila'
tabla.bind("<<TreeviewSelect>>", al_seleccionar_fila)